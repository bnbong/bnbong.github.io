"""Claude CLI adapter.

Invokes ``claude -p --output-format json [--json-schema <inline-json>]``,
feeding the rendered prompt through stdin. The ``--json-schema`` flag accepts
the schema JSON inline (not a file path). The JSON envelope's ``result``
field is extracted; when a schema is supplied and the result is valid JSON,
it is also returned in ``parsed``. All failures are captured in the returned
``AdapterResult`` so callers can decide whether to retry or surface the error.
"""

from __future__ import annotations

import json
import subprocess
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from ..errors import AdapterError
from .base import AdapterResult, invoke


@dataclass
class ClaudeAdapter:
    name: str = "claude"
    binary: str = "claude"
    model: str | None = None
    # None = no timeout. Overridable via config / per-call ``extra["timeout_sec"]``.
    timeout_sec: int | None = None

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
        cmd: list[str] = [self.binary, "-p", "--output-format", "json"]
        if self.model:
            cmd.extend(["--model", self.model])

        if schema is not None:
            cmd.extend(["--json-schema", json.dumps(schema, ensure_ascii=False)])

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
        except subprocess.TimeoutExpired:
            return AdapterResult(
                ok=False,
                text="",
                stderr=f"TIMEOUT after {timeout}s",
                cmd=cmd,
                exit_code=-1,
            )

        stdout = proc.stdout or ""
        stderr = proc.stderr or ""
        text, parsed = _extract_result(stdout, expects_json=schema is not None)

        ok = proc.returncode == 0 and bool(text)
        return AdapterResult(
            ok=ok,
            text=text or stdout,
            parsed=parsed,
            stderr=stderr,
            cmd=cmd,
            duration_ms=duration_ms,
            exit_code=proc.returncode,
        )


def _extract_result(stdout: str, *, expects_json: bool) -> tuple[str, dict | None]:
    """Parse the claude envelope.

    The CLI emits a JSON object. With ``--json-schema`` the validated payload
    arrives under ``structured_output`` (and ``result`` is empty). Without a
    schema, the free-form text lives in ``result``.
    """
    stripped = stdout.strip()
    if not stripped:
        return "", None
    try:
        envelope = json.loads(stripped)
    except json.JSONDecodeError:
        return stripped, None

    if expects_json and isinstance(envelope, dict):
        structured = envelope.get("structured_output")
        if isinstance(structured, dict):
            return json.dumps(structured, ensure_ascii=False), structured
        if isinstance(structured, str):
            try:
                parsed = json.loads(structured)
            except json.JSONDecodeError:
                return structured, None
            if isinstance(parsed, dict):
                return structured, parsed
            return structured, None

    if isinstance(envelope, dict) and "result" in envelope:
        result = envelope["result"]
    else:
        result = envelope

    if isinstance(result, dict):
        return json.dumps(result, ensure_ascii=False), result
    if isinstance(result, str):
        if expects_json:
            try:
                parsed = json.loads(result)
            except json.JSONDecodeError:
                return result, None
            if isinstance(parsed, dict):
                return result, parsed
            return result, None
        return result, None
    return json.dumps(result, ensure_ascii=False), None


def require_binary(binary: str) -> None:
    from shutil import which

    if which(binary) is None:
        raise AdapterError(f"{binary!r} not found on PATH.")


def _coerce_timeout(value: Any) -> int | None:
    """Accept int/str/None and map falsy values to "no timeout"."""
    if value in (None, "", 0, "0"):
        return None
    return int(value)
