"""`blogflow publish` — write the final body into the target post file."""

from __future__ import annotations

from datetime import date, datetime
from pathlib import Path

import click

from .. import frontmatter as fm_mod
from .. import publish as publish_mod
from .. import state
from . import _context as ctx_mod


@click.command("publish")
@click.option(
    "--session", "session_id", default=None, help="Session id (defaults to latest)."
)
@click.option(
    "--post-path",
    "post_path_override",
    default=None,
    help=(
        "Set or override the target post path for this session. Useful when "
        "`blogflow init` was run without `--post-path`. Path must live under "
        "docs/blog/posts/ and end in .md."
    ),
)
def publish_cmd(session_id: str | None, post_path_override: str | None) -> None:
    ctx = ctx_mod.build_context()
    session = ctx.store.resolve_latest(session_id)
    session_dir = ctx.store.session_path(session.id)
    blog_dir = str(ctx.config.get("blog_dir") or publish_mod.DEFAULT_BLOG_DIR)

    if post_path_override is not None:
        # Validate first so a bad path doesn't mutate the session silently.
        publish_mod.validate_post_path(ctx.repo_root, post_path_override, blog_dir)
        if session.target_post_path and session.target_post_path != post_path_override:
            click.echo(
                f"overriding target_post_path: "
                f"{session.target_post_path} → {post_path_override}"
            )
        session.target_post_path = post_path_override
        ctx.store.save(session)

    final_path = session_dir / "outputs" / "final.md"
    publish_mod.guard_publish(
        status=session.status,
        expected_status=state.STATUS_APPROVED,
        target_post_path=session.target_post_path,
        final_path=final_path,
    )

    post_path = publish_mod.validate_post_path(
        ctx.repo_root, session.target_post_path, blog_dir
    )
    publish_cfg = ctx.config.get("publish") or {}
    ensure_draft_false = bool(publish_cfg.get("ensure_draft_false", True))
    update_updated_date = bool(publish_cfg.get("update_updated_date", True))

    # Warn if we're about to replace a non-trivial existing body. The author
    # can Ctrl+C, restore from git, and merge manually instead of losing content.
    if post_path.exists():
        try:
            existing = fm_mod.read(post_path)
            if len((existing.body or "").strip()) > 40:
                click.echo(
                    f"warning: {session.target_post_path} has an existing body "
                    f"(~{len(existing.body)} chars) that will be replaced."
                )
                click.echo(
                    "         Review with `git diff` after publish; restore "
                    "hand-written sections if needed."
                )
        except Exception:
            pass

    publish_mod.merge_final_into_post(
        post_path,
        final_path.read_text(encoding="utf-8"),
        today=date.today(),
        ensure_draft_false=ensure_draft_false,
        topic=session.topic,
        author=ctx.author(),
        update_updated_date=update_updated_date,
    )

    state.transition(session, state.STATUS_PUBLISHED)
    session.published_at = datetime.now().isoformat(timespec="seconds")
    ctx.store.save(session)

    session_rel = ctx_mod.session_rel_path(ctx, session)
    rel_post = Path(session.target_post_path)
    click.echo(f"published → {rel_post}")
    click.echo("")
    click.echo("suggested git commands (run yourself when ready):")
    for cmd in publish_mod.suggested_git_commands(
        rel_post, session_rel, repo_root=ctx.repo_root
    ):
        click.echo(f"  {cmd}")
