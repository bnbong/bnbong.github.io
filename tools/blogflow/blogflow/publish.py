"""Publish-phase file operations. Writes to the target post file but never touches Git."""

from __future__ import annotations

from datetime import date
from pathlib import Path
from typing import Any

from . import frontmatter as fm_mod
from .errors import PublishError
from .models import Frontmatter


def validate_post_path(repo_root: Path, rel_path: str) -> Path:
    """Ensure the target post path lives under docs/blog/posts/ and ends with .md."""
    blog_root = (repo_root / "docs" / "blog" / "posts").resolve()
    target = (repo_root / rel_path).resolve()
    try:
        target.relative_to(blog_root)
    except ValueError as exc:
        raise PublishError(
            f"Post path {rel_path!r} must live under docs/blog/posts/."
        ) from exc
    if target.suffix != ".md":
        raise PublishError(f"Post path {rel_path!r} must have a .md extension.")
    return target


def build_skeleton(topic: str, *, today: date, author: str) -> Frontmatter:
    return Frontmatter(
        raw={
            "title": topic,
            "description": topic,
            "authors": [author],
            "date": {"created": today.isoformat(), "updated": today.isoformat()},
            "categories": [],
            "tags": [],
            "comments": True,
        },
        body="",
    )


def merge_final_into_post(
    post_path: Path,
    final_body: str,
    *,
    today: date,
    ensure_draft_false: bool,
    topic: str,
    author: str,
) -> None:
    if post_path.exists():
        fm = fm_mod.read(post_path)
    else:
        fm = build_skeleton(topic, today=today, author=author)
    fm.body = final_body.lstrip("\n")
    fm.ensure_published(today=today, ensure_draft_false=ensure_draft_false)
    fm_mod.write_atomic(post_path, fm)


def suggested_git_commands(post_path: Path, session_dir_rel: str) -> list[str]:
    rel_post = post_path.as_posix()
    return [
        f"git add {rel_post} {session_dir_rel}",
        f'git commit -m "post: $(basename {rel_post} .md)"',
        "git push origin master",
    ]


def guard_publish(
    *,
    status: str,
    expected_status: str,
    target_post_path: str | None,
    final_path: Path,
) -> None:
    if status != expected_status:
        raise PublishError(
            f"Session must be {expected_status!r}, got {status!r}. Run `blogflow approve` first."
        )
    if not target_post_path:
        raise PublishError(
            "Session has no target_post_path set. Use `blogflow init --post-path ...` next time."
        )
    if not final_path.exists():
        raise PublishError(
            f"Final output not found at {final_path}. Run `blogflow finalize` first."
        )


def _unused(_: Any) -> None:  # pragma: no cover
    pass
