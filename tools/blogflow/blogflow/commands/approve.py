"""`blogflow approve` — mark the final output as approved for publish."""

from __future__ import annotations

from datetime import datetime

import click

from .. import state
from . import _context as ctx_mod


@click.command("approve")
@click.option(
    "--session", "session_id", default=None, help="Session id (defaults to latest)."
)
def approve_cmd(session_id: str | None) -> None:
    ctx = ctx_mod.build_context()
    session = ctx.store.resolve_latest(session_id)
    session_dir = ctx.store.session_path(session.id)

    if session.status != state.STATUS_FINAL_READY:
        raise click.ClickException(
            f"Session must be in {state.STATUS_FINAL_READY!r}; got {session.status!r}. "
            f"Next: {ctx_mod.next_hint(session.status)}"
        )

    final_path = session_dir / "outputs" / "final.md"
    if not final_path.exists():
        raise click.ClickException(
            f"Final output missing: {final_path}. Run `blogflow finalize` first."
        )

    state.transition(session, state.STATUS_APPROVED)
    session.approved_at = datetime.now().isoformat(timespec="seconds")
    ctx.store.save(session)

    click.echo(f"approved: {session.id} at {session.approved_at}")
    click.echo("Next: blogflow publish")
