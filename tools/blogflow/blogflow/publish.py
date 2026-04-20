"""Publish-phase file operations. Writes to the target post file but never touches Git."""

from __future__ import annotations

import subprocess
from datetime import date
from pathlib import Path
from typing import Any

from . import frontmatter as fm_mod
from .errors import PublishError
from .models import Frontmatter


DEFAULT_BLOG_DIR = "docs/blog/posts"


def validate_post_path(
    repo_root: Path, rel_path: str, blog_dir: str = DEFAULT_BLOG_DIR
) -> Path:
    """Ensure the target post path lives under the configured blog dir and ends with .md.

    ``blog_dir`` defaults to ``docs/blog/posts`` for callers that do not thread
    the full config through (e.g. unit tests). Callers that have access to
    ``ctx.config`` should pass ``config["blog_dir"]`` so that overriding
    ``blog_dir`` in ``.blogflow/config.yaml`` actually takes effect.
    """
    blog_root = (repo_root / blog_dir).resolve()
    target = (repo_root / rel_path).resolve()
    try:
        target.relative_to(blog_root)
    except ValueError as exc:
        raise PublishError(
            f"Post path {rel_path!r} must live under {blog_dir}/."
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
    update_updated_date: bool = True,
) -> None:
    if post_path.exists():
        fm = fm_mod.read(post_path)
    else:
        fm = build_skeleton(topic, today=today, author=author)
    fm.body = final_body.lstrip("\n")
    fm.ensure_published(
        today=today,
        ensure_draft_false=ensure_draft_false,
        update_updated_date=update_updated_date,
    )
    fm_mod.write_atomic(post_path, fm)


def suggested_git_commands(
    post_path: Path,
    session_dir_rel: str,
    *,
    repo_root: Path | None = None,
) -> list[str]:
    """Return copy-pasteable `git add / commit / push` suggestions.

    The push command targets whatever branch the repo is currently on. If we
    can't detect the branch (no git, detached HEAD, repo_root not passed), we
    emit a bare `git push` so the user's tracking config decides — much safer
    than hardcoding `master`/`main` and misleading users on the other layout.
    """
    rel_post = post_path.as_posix()
    branch = _detect_current_branch(repo_root) if repo_root else None
    push_cmd = f"git push origin {branch}" if branch else "git push"
    return [
        f"git add {rel_post} {session_dir_rel}",
        f'git commit -m "post: $(basename {rel_post} .md)"',
        push_cmd,
    ]


def _detect_current_branch(repo_root: Path) -> str | None:
    try:
        result = subprocess.run(
            ["git", "-C", str(repo_root), "rev-parse", "--abbrev-ref", "HEAD"],
            capture_output=True,
            text=True,
            timeout=5,
            check=False,
        )
    except (OSError, subprocess.TimeoutExpired):
        return None
    if result.returncode != 0:
        return None
    branch = result.stdout.strip()
    # `HEAD` means detached — no branch to push to.
    if not branch or branch == "HEAD":
        return None
    return branch


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
            "Session has no target_post_path set. Either re-run publish with "
            "`blogflow publish --post-path <docs/blog/posts/...>` to set it "
            "retroactively, or pass `--post-path` to `blogflow init` next time."
        )
    if not final_path.exists():
        raise PublishError(
            f"Final output not found at {final_path}. Run `blogflow finalize` first."
        )


def _unused(_: Any) -> None:  # pragma: no cover
    pass
