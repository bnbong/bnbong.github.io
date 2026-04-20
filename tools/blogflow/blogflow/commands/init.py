"""`blogflow init` — create a new session."""

from __future__ import annotations

import click

from ..publish import DEFAULT_BLOG_DIR, validate_post_path
from ..state import Session, new_session_id, slugify
from . import _context as ctx_mod


@click.command("init")
@click.option("--topic", required=True, help="Topic title for the post.")
@click.option(
    "--post-path",
    "post_path",
    default=None,
    help="Target post file relative to repo root (must live under docs/blog/posts/).",
)
@click.option(
    "--from-idea",
    "from_idea",
    default=None,
    help="Optional reference back to an ideas/<ts>.yaml entry id — stored as-is in session metadata.",
)
def init_cmd(topic: str, post_path: str | None, from_idea: str | None) -> None:
    """Create a new session directory and YAML under `.blogflow/sessions/`."""
    ctx = ctx_mod.build_context()

    if post_path:
        blog_dir = str(ctx.config.get("blog_dir") or DEFAULT_BLOG_DIR)
        validate_post_path(ctx.repo_root, post_path, blog_dir)

    sid = new_session_id(topic, existing=set(ctx.store.list_sessions()))
    session = Session(
        id=sid,
        topic=topic,
        slug=slugify(topic),
        target_post_path=post_path,
    )
    ctx.store.create(session)

    if from_idea:
        meta_path = ctx.store.session_path(sid) / "user" / "origin.yaml"
        meta_path.parent.mkdir(parents=True, exist_ok=True)
        meta_path.write_text(f"from_idea: {from_idea}\n", encoding="utf-8")

    click.echo(f"Session created: {sid}")
    click.echo(f"  topic: {topic}")
    if post_path:
        click.echo(f"  target_post_path: {post_path}")
    click.echo("Next: blogflow brief")
