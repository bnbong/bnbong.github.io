"""`blogflow brief` — structured learning brief + author questions."""

from __future__ import annotations

import json

import click

from .. import prompts, state
from ..errors import AdapterError
from ..schemas import BRIEF_SCHEMA
from . import _context as ctx_mod


@click.command("brief")
@click.option(
    "--session", "session_id", default=None, help="Session id (defaults to latest)."
)
def brief_cmd(session_id: str | None) -> None:
    ctx = ctx_mod.build_context()
    session = ctx.store.resolve_latest(session_id)
    session_dir = ctx.store.session_path(session.id)

    if session.status != state.STATUS_INITIATED:
        raise click.ClickException(
            f"Session must be in {state.STATUS_INITIATED!r}; got {session.status!r}. "
            f"Next: {ctx_mod.next_hint(session.status)}"
        )

    prompt = prompts.render(
        "brief",
        {
            "author": ctx.author(),
            "default_category": ctx.default_category(),
            "session": session,
            "recent_titles": ctx.recent_post_titles(),
        },
        ctx.repo_root,
    )
    ctx_mod.write_prompt(session_dir, "brief", prompt)

    adapter = ctx.claude_adapter()
    result = adapter.run(
        prompt,
        schema=BRIEF_SCHEMA,
        log_dir=session_dir / "logs",
        stage="brief",
    )
    if not result.ok:
        raise AdapterError(
            f"claude brief failed (exit={result.exit_code}). See log under {session_dir / 'logs'}."
        )

    parsed = result.parsed or _loose_parse(result.text)
    if parsed is None:
        raise AdapterError("Could not parse brief JSON. See log.")

    ctx_mod.write_json(session_dir / "outputs" / "brief.json", parsed)
    ctx_mod.write_json(session_dir / "schemas" / "brief.schema.json", BRIEF_SCHEMA)

    state.transition(session, state.STATUS_BRIEF_READY)
    state.transition(session, state.STATUS_AWAITING_ANSWERS)
    ctx.store.save(session)

    click.echo(f"brief → {session_dir / 'outputs' / 'brief.json'}")
    qs = parsed.get("questions") or []
    click.echo(f"{len(qs)} question(s) for the author.")
    click.echo("Next: blogflow answer --interactive   (or --file answers.yaml)")


def _loose_parse(text: str) -> dict | None:
    try:
        data = json.loads(text)
    except json.JSONDecodeError:
        return None
    return data if isinstance(data, dict) else None
