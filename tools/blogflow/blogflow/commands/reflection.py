"""`blogflow reflection` — record the author's optional closing reflection."""

from __future__ import annotations

import os
import shlex
import subprocess
import tempfile
from pathlib import Path

import click

from .. import prompts, state
from . import _context as ctx_mod


@click.command("reflection")
@click.option(
    "--session", "session_id", default=None, help="Session id (defaults to latest)."
)
@click.option("--skip", is_flag=True, default=False, help="Skip the reflection stage.")
@click.option("--text", default=None, help="Inline reflection text.")
@click.option(
    "--file",
    "file_path",
    type=click.Path(path_type=Path, exists=True),
    default=None,
    help="Path to a markdown file to use as the reflection.",
)
def reflection_cmd(
    session_id: str | None,
    skip: bool,
    text: str | None,
    file_path: Path | None,
) -> None:
    ctx = ctx_mod.build_context()
    session = ctx.store.resolve_latest(session_id)
    session_dir = ctx.store.session_path(session.id)

    if session.status != state.STATUS_AWAITING_REFLECTION:
        raise click.ClickException(
            f"Session must be in {state.STATUS_AWAITING_REFLECTION!r}; got {session.status!r}. "
            f"Next: {ctx_mod.next_hint(session.status)}"
        )

    content = _resolve_content(
        ctx_ref=ctx, session=session, skip=skip, text=text, file_path=file_path
    )

    reflection_path = session_dir / "user" / "reflection.md"
    if content:
        reflection_path.parent.mkdir(parents=True, exist_ok=True)
        reflection_path.write_text(content, encoding="utf-8")
        session.reflection_skipped = False
        click.echo(f"reflection → {reflection_path}")
    else:
        session.reflection_skipped = True
        click.echo("reflection skipped.")

    state.transition(session, state.STATUS_FINAL_READY)
    ctx.store.save(session)
    click.echo("Next: blogflow finalize")


def _resolve_content(
    *,
    ctx_ref,
    session,
    skip: bool,
    text: str | None,
    file_path: Path | None,
) -> str:
    if skip:
        return ""
    if text is not None:
        return text.strip()
    if file_path is not None:
        return file_path.read_text(encoding="utf-8").strip()
    return _editor_flow(ctx_ref, session)


def _editor_flow(ctx_ref, session) -> str:
    primer = prompts.render(
        "reflection",
        {"author": ctx_ref.author(), "session": session},
        ctx_ref.repo_root,
    )
    header = (
        "# Write your reflection below (save + close to submit, leave empty to skip).\n"
        "# Lines starting with # are ignored.\n"
    )
    primer_comment = "\n".join(
        f"# {line}" if line else "#" for line in primer.splitlines()
    )
    template = header + primer_comment + "\n\n"

    editor_env = os.environ.get("EDITOR") or "vi"
    editor_cmd = shlex.split(editor_env) or ["vi"]
    fd, tmp = tempfile.mkstemp(prefix="blogflow-reflection-", suffix=".md")
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            f.write(template)
        subprocess.run([*editor_cmd, tmp], check=False)
        raw = Path(tmp).read_text(encoding="utf-8")
    finally:
        try:
            os.unlink(tmp)
        except FileNotFoundError:
            pass

    lines = [ln for ln in raw.splitlines() if not ln.lstrip().startswith("#")]
    return "\n".join(lines).strip()
