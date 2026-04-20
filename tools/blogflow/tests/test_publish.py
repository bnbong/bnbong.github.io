from __future__ import annotations

from datetime import date
from pathlib import Path

import pytest

from blogflow import publish as P
from blogflow.errors import PublishError


def test_validate_post_path_accepts_blog_post(repo_root: Path):
    rel = "docs/blog/posts/20250101/new.md"
    result = P.validate_post_path(repo_root, rel)
    assert result == (repo_root / rel).resolve()


def test_validate_post_path_rejects_escape(repo_root: Path):
    with pytest.raises(PublishError):
        P.validate_post_path(repo_root, "../outside.md")


def test_validate_post_path_rejects_non_md(repo_root: Path):
    with pytest.raises(PublishError):
        P.validate_post_path(repo_root, "docs/blog/posts/foo.txt")


def test_validate_post_path_rejects_non_blog(repo_root: Path):
    with pytest.raises(PublishError):
        P.validate_post_path(repo_root, "docs/index.md")


def test_merge_final_creates_skeleton(repo_root: Path):
    target = repo_root / "docs" / "blog" / "posts" / "20260420" / "new.md"
    P.merge_final_into_post(
        target,
        "## Intro\n\nHello.\n",
        today=date(2026, 4, 20),
        ensure_draft_false=True,
        topic="New Post",
        author="bnbong",
    )
    text = target.read_text(encoding="utf-8")
    assert "title: New Post" in text
    assert "## Intro" in text
    assert "created: '2026-04-20'" in text or "created: 2026-04-20" in text


def test_merge_final_updates_existing(sample_post: Path):
    P.merge_final_into_post(
        sample_post,
        "## Updated\n\nrewritten.\n",
        today=date(2026, 4, 20),
        ensure_draft_false=True,
        topic="Sample Post",
        author="bnbong",
    )
    text = sample_post.read_text(encoding="utf-8")
    assert "## Updated" in text
    assert "Hello, world." not in text
    assert "created: 2025-01-01" in text or "created: '2025-01-01'" in text
    assert "updated: '2026-04-20'" in text or "updated: 2026-04-20" in text


def test_guard_publish_requires_approved():
    with pytest.raises(PublishError):
        P.guard_publish(
            status="final_ready",
            expected_status="approved",
            target_post_path="docs/blog/posts/x.md",
            final_path=Path("/nonexistent"),
        )


def test_guard_publish_requires_target(tmp_path: Path):
    final = tmp_path / "final.md"
    final.write_text("body", encoding="utf-8")
    with pytest.raises(PublishError):
        P.guard_publish(
            status="approved",
            expected_status="approved",
            target_post_path=None,
            final_path=final,
        )


def test_strip_provenance_markers_removes_supported_and_assumed():
    """Final.md / published posts must never expose internal `[SUPPORTED:<label>]`
    or `[ASSUMED]` tags to readers — they are audit markers used only between
    draft and review stages."""
    from blogflow.commands.finalize import strip_provenance_markers

    raw = (
        "IPv4 헤더는 기본 20 바이트이다 [SUPPORTED:RFC 791].\n"
        "이 주장은 아직 검증되지 않았다 [ASSUMED].\n"
        "여러 태그가 한 문단에 섞여도 [SUPPORTED:IANA] [ASSUMED] 제거된다.\n"
    )
    cleaned = strip_provenance_markers(raw)
    assert "[SUPPORTED:" not in cleaned
    assert "[ASSUMED]" not in cleaned
    # Prose must still read naturally — no double spaces or orphan punctuation.
    assert "20 바이트이다." in cleaned
    assert "검증되지 않았다." in cleaned
    assert "한 문단에 섞여도 제거된다." in cleaned


def test_suggested_git_commands_format(tmp_path: Path):
    cmds = P.suggested_git_commands(
        Path("docs/blog/posts/x.md"), ".blogflow/sessions/abc"
    )
    assert any(c.startswith("git add ") for c in cmds)
    assert any("git commit -m" in c for c in cmds)
    assert any("git push" in c for c in cmds)
