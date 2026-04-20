"""`blogflow answer` — record author answers to the brief questions."""

from __future__ import annotations

from pathlib import Path
from typing import Any

import click

from .. import state
from ..models import Brief
from . import _context as ctx_mod


@click.command("answer")
@click.option(
    "--session", "session_id", default=None, help="Session id (defaults to latest)."
)
@click.option(
    "--file", "file_path", type=click.Path(path_type=Path, exists=True), default=None
)
@click.option("--interactive", is_flag=True, default=False)
def answer_cmd(
    session_id: str | None, file_path: Path | None, interactive: bool
) -> None:
    ctx = ctx_mod.build_context()
    session = ctx.store.resolve_latest(session_id)
    session_dir = ctx.store.session_path(session.id)

    if session.status != state.STATUS_AWAITING_ANSWERS:
        raise click.ClickException(
            f"Session must be in {state.STATUS_AWAITING_ANSWERS!r}; got {session.status!r}. "
            f"Next: {ctx_mod.next_hint(session.status)}"
        )

    brief_path = session_dir / "outputs" / "brief.json"
    if not brief_path.exists():
        raise click.ClickException(f"Brief output missing: {brief_path}")
    brief = Brief.from_dict(ctx_mod.read_json(brief_path))

    if not brief.questions:
        answers: dict[str, str] = {}
    elif file_path:
        answers = _load_answers_file(file_path, brief)
    elif interactive:
        answers = _prompt_interactive(brief)
    else:
        raise click.ClickException("Provide --interactive or --file <answers.yaml>.")

    ctx_mod.write_yaml(session_dir / "user" / "answers.yaml", {"answers": answers})

    state.transition(session, state.STATUS_DRAFT_READY)
    ctx.store.save(session)
    click.echo(f"answers → {session_dir / 'user' / 'answers.yaml'}")
    click.echo("Next: blogflow draft")


def _load_answers_file(path: Path, brief: Brief) -> dict[str, str]:
    data: Any = ctx_mod.read_yaml(path)
    raw = data.get("answers") if isinstance(data.get("answers"), dict) else data
    if not isinstance(raw, dict):
        raise click.ClickException(
            f"{path} must contain a mapping of question_id → answer text."
        )
    valid_ids = {q.id for q in brief.questions}
    out: dict[str, str] = {}
    for qid, val in raw.items():
        if qid not in valid_ids:
            click.echo(f"warning: unknown question id {qid!r} in {path}; skipping")
            continue
        out[str(qid)] = str(val)
    missing = valid_ids - set(out)
    if missing:
        click.echo(f"warning: no answer recorded for: {sorted(missing)}")
    return out


def _prompt_interactive(brief: Brief) -> dict[str, str]:
    answers: dict[str, str] = {}
    for q in brief.questions:
        click.echo("")
        click.echo(f"[{q.id}] {q.text}")
        if q.why:
            click.echo(f"  (왜: {q.why})")
        val = click.prompt("  답변 (공백 = skip)", default="", show_default=False)
        if val.strip():
            answers[q.id] = val.strip()
    return answers
