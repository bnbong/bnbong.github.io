"""Codex CLI adapter.

Shells out to ``codex exec`` for both draft generation and review. Codex has no
native JSON-schema mode, so prompts must end with a ``GATE: APPROVED|REVISE|BLOCK``
marker when a decision is needed; parsing that marker is the caller's job — the
adapter only returns the raw text.

``mode`` in ``extra`` controls which sandbox is used:

- ``"exec"`` (default) — ``sandbox_exec`` (``workspace-write``), used for any
  write-enabled stage.
- ``"review"`` — ``sandbox_review`` (``read-only``), used for factual-check
  stages that must not mutate the workspace.
"""

from __future__ import annotations

import subprocess
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from .base import AdapterResult, invoke


@dataclass
class CodexAdapter:
    name: str = "codex"
    binary: str = "codex"
    model: str | None = None
    sandbox_exec: str = "workspace-write"
    sandbox_review: str = "read-only"
    # None = no timeout. Overridable via config / per-call ``extra["timeout_sec"]``.
    timeout_sec: int | None = None
    # Codex respects the user's `~/.codex/config.toml` reasoning effort, which
    # defaults to `xhigh` on many installs and makes a full-draft review run
    # 10+ minutes. Blogflow overrides this per-invocation to keep review and
    # draft turns interactive; users can raise it via config if needed.
    reasoning_effort: str | None = "medium"

    def run(
        self,
        prompt: str,
        *,
        schema: dict | None = None,
        log_dir: Path,
        stage: str,
        extra: dict[str, Any] | None = None,
    ) -> AdapterResult:
        extra = extra or {}
        mode = extra.get("mode", "exec")
        sandbox = extra.get(
            "sandbox",
            self.sandbox_review if mode == "review" else self.sandbox_exec,
        )

        cmd: list[str] = [self.binary, "exec", "-s", str(sandbox)]
        if self.model:
            cmd.extend(["--model", self.model])

        effort = extra.get("reasoning_effort", self.reasoning_effort)
        if effort:
            cmd.extend(["-c", f"model_reasoning_effort={effort}"])

        for flag in extra.get("extra_args", []) or []:
            cmd.append(str(flag))

        timeout = _coerce_timeout(extra.get("timeout_sec", self.timeout_sec))

        try:
            proc, duration_ms = invoke(
                cmd,
                stdin_text=prompt,
                timeout_sec=timeout,
                log_dir=log_dir,
                stage=stage,
                adapter_name=self.name,
            )
        except subprocess.TimeoutExpired as exc:
            return AdapterResult(
                ok=False,
                text=(exc.stdout or "") if isinstance(exc.stdout, str) else "",
                stderr=f"TIMEOUT after {timeout}s",
                cmd=cmd,
                exit_code=-1,
            )

        stdout = proc.stdout or ""
        stderr = proc.stderr or ""
        ok = proc.returncode == 0 and bool(stdout.strip())
        return AdapterResult(
            ok=ok,
            text=stdout,
            parsed=None,
            stderr=stderr,
            cmd=cmd,
            duration_ms=duration_ms,
            exit_code=proc.returncode,
        )


GATE_APPROVED = "APPROVED"
GATE_REVISE = "REVISE"
GATE_BLOCK = "BLOCK"
GATE_UNCLEAR = "UNCLEAR"


def parse_gate(text: str) -> str:
    """Find the last ``GATE:`` marker in the text and return the decision."""
    last: str | None = None
    for line in text.splitlines():
        stripped = line.strip()
        if stripped.upper().startswith("GATE:"):
            last = stripped.split(":", 1)[1].strip().upper()
    if last in {GATE_APPROVED, GATE_REVISE, GATE_BLOCK}:
        return last
    return GATE_UNCLEAR


def _coerce_timeout(value: Any) -> int | None:
    """Accept int/str/None and map falsy values to "no timeout"."""
    if value in (None, "", 0, "0"):
        return None
    return int(value)
