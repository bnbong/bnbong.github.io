from __future__ import annotations

import json
import subprocess
from pathlib import Path
from unittest.mock import patch

import pytest

from blogflow.adapters import base as base_mod
from blogflow.adapters.claude import ClaudeAdapter
from blogflow.adapters.codex import (
    GATE_APPROVED,
    GATE_BLOCK,
    GATE_REVISE,
    GATE_UNCLEAR,
    CodexAdapter,
    parse_gate,
)
from blogflow.errors import AdapterError


def _fake_completed(stdout: str = "", stderr: str = "", returncode: int = 0):
    return subprocess.CompletedProcess(
        args=[], returncode=returncode, stdout=stdout, stderr=stderr
    )


def test_invoke_writes_log(tmp_path: Path):
    with patch.object(base_mod.subprocess, "run", return_value=_fake_completed("hi")):
        proc, dur = base_mod.invoke(
            ["fake"],
            stdin_text="prompt",
            timeout_sec=5,
            log_dir=tmp_path / "logs",
            stage="brief",
            adapter_name="claude",
        )
    assert proc.stdout == "hi"
    logs = list((tmp_path / "logs").glob("brief-claude-*.log"))
    assert len(logs) == 1
    content = logs[0].read_text(encoding="utf-8")
    assert "exit_code: 0" in content
    assert "hi" in content


def test_claude_adapter_parses_json_result(tmp_path: Path):
    schema = {
        "type": "object",
        "required": ["x"],
        "properties": {"x": {"type": "string"}},
    }
    envelope = {"type": "result", "result": json.dumps({"x": "ok"})}
    with patch.object(
        base_mod.subprocess, "run", return_value=_fake_completed(json.dumps(envelope))
    ) as mock_run:
        adapter = ClaudeAdapter(timeout_sec=5)
        result = adapter.run(
            "prompt",
            schema=schema,
            log_dir=tmp_path / "logs",
            stage="brief",
        )
    assert result.ok
    assert result.parsed == {"x": "ok"}
    # `--json-schema` must carry the inline JSON (not a file path) so the
    # claude CLI can parse it — passing a path causes the CLI to hang.
    called_cmd = mock_run.call_args.args[0]
    assert "--json-schema" in called_cmd
    schema_arg = called_cmd[called_cmd.index("--json-schema") + 1]
    assert json.loads(schema_arg) == schema
    assert "--output-format" in called_cmd and "json" in called_cmd


def test_claude_adapter_reads_structured_output_field(tmp_path: Path):
    """When --json-schema is used, the validated payload lives in
    `structured_output`, not `result` (which is empty). The adapter must
    pick up the right field or downstream stages see an empty brief."""
    schema = {
        "type": "object",
        "required": ["goal"],
        "properties": {"goal": {"type": "string"}},
    }
    envelope = {
        "type": "result",
        "result": "",
        "structured_output": {"goal": "understand IPv4"},
    }
    with patch.object(
        base_mod.subprocess, "run", return_value=_fake_completed(json.dumps(envelope))
    ):
        adapter = ClaudeAdapter(timeout_sec=5)
        result = adapter.run(
            "prompt",
            schema=schema,
            log_dir=tmp_path / "logs",
            stage="brief",
        )
    assert result.ok
    assert result.parsed == {"goal": "understand IPv4"}


def test_claude_adapter_disables_timeout_when_none(tmp_path: Path):
    """`timeout_sec=None` (blogflow's default) must pass `timeout=None` to
    subprocess, not a number — LLM turns vary wildly and users rely on
    Ctrl+C, not a hard ceiling."""
    with patch.object(
        base_mod.subprocess, "run", return_value=_fake_completed('{"result":"ok"}')
    ) as mock_run:
        adapter = ClaudeAdapter(timeout_sec=None)
        adapter.run("prompt", log_dir=tmp_path / "logs", stage="brief")
    assert mock_run.call_args.kwargs["timeout"] is None


def test_codex_adapter_disables_timeout_when_none(tmp_path: Path):
    with patch.object(
        base_mod.subprocess, "run", return_value=_fake_completed("text")
    ) as mock_run:
        adapter = CodexAdapter(timeout_sec=None)
        adapter.run(
            "prompt",
            log_dir=tmp_path / "logs",
            stage="review",
            extra={"mode": "review"},
        )
    assert mock_run.call_args.kwargs["timeout"] is None


def test_claude_adapter_handles_nonzero_exit(tmp_path: Path):
    with patch.object(
        base_mod.subprocess, "run", return_value=_fake_completed("", "boom", 2)
    ):
        adapter = ClaudeAdapter(timeout_sec=5)
        result = adapter.run("prompt", log_dir=tmp_path / "logs", stage="brief")
    assert not result.ok
    assert result.exit_code == 2
    assert "boom" in result.stderr


def test_claude_adapter_without_schema_returns_text(tmp_path: Path):
    envelope = {"result": "plain text"}
    with patch.object(
        base_mod.subprocess, "run", return_value=_fake_completed(json.dumps(envelope))
    ):
        adapter = ClaudeAdapter(timeout_sec=5)
        result = adapter.run("prompt", log_dir=tmp_path / "logs", stage="finalize")
    assert result.ok
    assert result.text == "plain text"
    assert result.parsed is None


def test_codex_adapter_exec_default_sandbox(tmp_path: Path):
    with patch.object(
        base_mod.subprocess,
        "run",
        return_value=_fake_completed("review text\nGATE: APPROVED"),
    ) as mock_run:
        adapter = CodexAdapter(timeout_sec=5)
        result = adapter.run("prompt", log_dir=tmp_path / "logs", stage="review")
    called_cmd = mock_run.call_args.args[0]
    assert called_cmd[:2] == ["codex", "exec"]
    assert "-s" in called_cmd and "workspace-write" in called_cmd
    assert result.ok
    assert "GATE: APPROVED" in result.text


def test_codex_adapter_review_mode_uses_read_only(tmp_path: Path):
    """Issue 1: `mode=review` must pick the read-only sandbox but still use `codex exec`."""
    with patch.object(
        base_mod.subprocess, "run", return_value=_fake_completed("text\nGATE: REVISE")
    ) as mock_run:
        adapter = CodexAdapter(timeout_sec=5, sandbox_review="read-only")
        adapter.run(
            "prompt",
            log_dir=tmp_path / "logs",
            stage="review",
            extra={"mode": "review"},
        )
    called_cmd = mock_run.call_args.args[0]
    assert called_cmd[:2] == ["codex", "exec"]
    # -s read-only must appear and workspace-write must NOT be used
    assert "-s" in called_cmd
    assert "read-only" in called_cmd
    assert "workspace-write" not in called_cmd


def test_codex_adapter_exec_mode_uses_workspace_write(tmp_path: Path):
    with patch.object(
        base_mod.subprocess, "run", return_value=_fake_completed("text")
    ) as mock_run:
        adapter = CodexAdapter(timeout_sec=5)
        adapter.run(
            "prompt",
            log_dir=tmp_path / "logs",
            stage="draft",
            extra={"mode": "exec"},
        )
    called_cmd = mock_run.call_args.args[0]
    assert "workspace-write" in called_cmd
    assert "read-only" not in called_cmd


def test_codex_adapter_sets_reasoning_effort(tmp_path: Path):
    """The user's global `~/.codex/config.toml` can default to `xhigh`, which
    makes full-draft reviews take 10+ minutes. The adapter must emit
    `-c model_reasoning_effort=<value>` to override that per invocation."""
    with patch.object(
        base_mod.subprocess, "run", return_value=_fake_completed("text\nGATE: APPROVED")
    ) as mock_run:
        adapter = CodexAdapter(timeout_sec=5, reasoning_effort="medium")
        adapter.run(
            "prompt",
            log_dir=tmp_path / "logs",
            stage="review",
            extra={"mode": "review"},
        )
    called_cmd = mock_run.call_args.args[0]
    assert "-c" in called_cmd
    assert "model_reasoning_effort=medium" in called_cmd


def test_codex_adapter_skips_effort_flag_when_none(tmp_path: Path):
    """Setting reasoning_effort=None must defer to the user's global config
    — no `-c` override should be added."""
    with patch.object(
        base_mod.subprocess, "run", return_value=_fake_completed("text")
    ) as mock_run:
        adapter = CodexAdapter(timeout_sec=5, reasoning_effort=None)
        adapter.run("prompt", log_dir=tmp_path / "logs", stage="draft")
    called_cmd = mock_run.call_args.args[0]
    assert not any(a.startswith("model_reasoning_effort=") for a in called_cmd)


def test_invoke_raises_adapter_error_when_binary_missing(tmp_path: Path):
    """A missing `claude` / `codex` binary used to bubble up as a raw
    FileNotFoundError traceback — breaks first-run UX on machines that don't
    have both CLIs installed. Must surface as AdapterError with an actionable
    hint so the top-level CLI wrapper formats it cleanly."""
    with patch.object(base_mod.subprocess, "run", side_effect=FileNotFoundError()):
        with pytest.raises(AdapterError) as exc_info:
            base_mod.invoke(
                ["nonexistent-binary"],
                stdin_text=None,
                timeout_sec=None,
                log_dir=tmp_path / "logs",
                stage="brief",
                adapter_name="claude",
            )
    msg = str(exc_info.value)
    assert "nonexistent-binary" in msg
    assert "PATH" in msg
    # Log file must still be written so the failure is auditable.
    logs = list((tmp_path / "logs").glob("brief-claude-*.log"))
    assert len(logs) == 1


def test_parse_gate_variants():
    assert parse_gate("stuff\nGATE: APPROVED") == GATE_APPROVED
    assert parse_gate("stuff\nGATE: REVISE\n") == GATE_REVISE
    assert parse_gate("stuff\nGATE: BLOCK") == GATE_BLOCK
    assert parse_gate("no gate here") == GATE_UNCLEAR
    # Last wins
    assert parse_gate("GATE: APPROVED\nGATE: BLOCK") == GATE_BLOCK
