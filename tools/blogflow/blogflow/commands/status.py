"""`blogflow status` — show the latest session's state and next step."""

from __future__ import annotations

import click

from . import _context as ctx_mod


@click.command("status")
@click.option(
    "--session",
    "session_id",
    default=None,
    help="Specific session id (defaults to latest).",
)
def status_cmd(session_id: str | None) -> None:
    ctx = ctx_mod.build_context()
    session = ctx.store.resolve_latest(session_id)
    session_dir = ctx.store.session_path(session.id)

    click.echo(f"session:  {session.id}")
    click.echo(f"topic:    {session.topic}")
    click.echo(f"status:   {session.status}")
    click.echo(f"created:  {session.created_at}")
    click.echo(f"updated:  {session.updated_at}")
    if session.target_post_path:
        click.echo(f"target:   {session.target_post_path}")
    if session.review_gate:
        click.echo(f"gate:     {session.review_gate}")

    click.echo("")
    click.echo("artifacts:")
    for sub in ("prompts", "outputs", "user", "logs"):
        d = session_dir / sub
        if not d.exists():
            continue
        for p in sorted(d.iterdir()):
            click.echo(f"  {p.relative_to(session_dir)}")

    click.echo("")
    click.echo(f"next: {ctx_mod.next_hint(session.status)}")
