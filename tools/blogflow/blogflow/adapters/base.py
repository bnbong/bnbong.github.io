"""Adapter protocol + shared invocation helpers."""

from __future__ import annotations

import itertools
import os
import subprocess
import sys
import threading
import time
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Any, Protocol


@dataclass
class AdapterResult:
    ok: bool
    text: str
    parsed: dict | None = None
    stderr: str = ""
    cmd: list[str] = field(default_factory=list)
    duration_ms: int = 0
    exit_code: int = 0


class LLMAdapter(Protocol):
    name: str

    def run(
        self,
        prompt: str,
        *,
        schema: dict | None = None,
        log_dir: Path,
        stage: str,
        extra: dict[str, Any] | None = None,
    ) -> AdapterResult: ...


def invoke(
    cmd: list[str],
    *,
    stdin_text: str | None,
    timeout_sec: int | None,
    log_dir: Path,
    stage: str,
    adapter_name: str,
) -> tuple[subprocess.CompletedProcess, int]:
    """Run subprocess, persist log, return process + duration_ms.

    ``timeout_sec=None`` (or ``0``) disables the timeout entirely — the
    default for blogflow, since LLM turns vary wildly with network and post
    length, and a stuck process can always be killed with Ctrl+C.

    While the subprocess runs, show an elapsed-time spinner on stderr so the
    user knows the CLI is alive during multi-minute LLM calls. The spinner
    is suppressed when stderr isn't a TTY (tests, pipelines, redirected runs).
    """
    log_dir.mkdir(parents=True, exist_ok=True)
    ts = datetime.now().strftime("%Y%m%d-%H%M%S")
    log_path = log_dir / f"{stage}-{adapter_name}-{ts}.log"
    start = time.monotonic()
    spinner = _Spinner(f"{stage} · {adapter_name}")
    spinner.start()
    effective_timeout = timeout_sec if timeout_sec else None
    try:
        proc = subprocess.run(
            cmd,
            input=stdin_text,
            capture_output=True,
            text=True,
            timeout=effective_timeout,
            check=False,
            env=os.environ.copy(),
        )
    except subprocess.TimeoutExpired as exc:
        spinner.stop()
        duration = int((time.monotonic() - start) * 1000)
        _write_log(
            log_path,
            cmd=cmd,
            exit_code=-1,
            duration_ms=duration,
            stdout=(
                exc.stdout.decode()
                if isinstance(exc.stdout, bytes)
                else (exc.stdout or "")
            ),
            stderr=f"TIMEOUT after {effective_timeout}s",
        )
        raise
    finally:
        spinner.stop()
    duration = int((time.monotonic() - start) * 1000)
    _write_log(
        log_path,
        cmd=cmd,
        exit_code=proc.returncode,
        duration_ms=duration,
        stdout=proc.stdout or "",
        stderr=proc.stderr or "",
    )
    return proc, duration


class _Spinner:
    """Background thread that prints an elapsed-time spinner on stderr.

    No-ops when stderr is not a TTY so it stays invisible in tests, CI, and
    piped runs. Uses a carriage return to stay on a single line.
    """

    _FRAMES = "⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏"

    def __init__(self, label: str):
        self._label = label
        self._stop = threading.Event()
        self._thread: threading.Thread | None = None
        self._active = sys.stderr.isatty()

    def start(self) -> None:
        if not self._active:
            return
        self._thread = threading.Thread(target=self._loop, daemon=True)
        self._thread.start()

    def stop(self) -> None:
        if not self._active or self._thread is None:
            return
        self._stop.set()
        self._thread.join(timeout=0.5)
        try:
            sys.stderr.write("\r" + " " * 80 + "\r")
            sys.stderr.flush()
        except Exception:
            pass

    def _loop(self) -> None:
        frames = itertools.cycle(self._FRAMES)
        start = time.monotonic()
        while not self._stop.is_set():
            elapsed = int(time.monotonic() - start)
            mins, secs = divmod(elapsed, 60)
            try:
                sys.stderr.write(f"\r{next(frames)} {self._label}  {mins}:{secs:02d}")
                sys.stderr.flush()
            except Exception:
                return
            self._stop.wait(0.12)


def _write_log(
    path: Path,
    *,
    cmd: list[str],
    exit_code: int,
    duration_ms: int,
    stdout: str,
    stderr: str,
) -> None:
    lines = [
        f"# cmd: {cmd}",
        f"# exit_code: {exit_code}",
        f"# duration_ms: {duration_ms}",
        "## stdout",
        stdout,
        "## stderr",
        stderr,
    ]
    path.write_text("\n".join(lines), encoding="utf-8")
