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


def test_suggested_git_commands_uses_detected_branch(tmp_path: Path, monkeypatch):
    """The push hint must not hardcode a branch — detect whichever branch the
    repo is currently on, or fall back to a bare `git push` if detection fails.
    Hardcoding `master` misled users on repos whose default is `main`."""
    import subprocess as sp

    captured: dict = {}

    def fake_run(argv, capture_output=False, text=False, timeout=None, check=False):
        captured["argv"] = argv
        return sp.CompletedProcess(args=argv, returncode=0, stdout="feature-x\n", stderr="")

    monkeypatch.setattr(P.subprocess, "run", fake_run)
    cmds = P.suggested_git_commands(
        Path("docs/blog/posts/x.md"),
        ".blogflow/sessions/abc",
        repo_root=tmp_path,
    )
    assert "git push origin feature-x" in cmds, cmds
    # Must have invoked `git rev-parse --abbrev-ref HEAD` on the given root.
    assert "rev-parse" in captured["argv"]
    assert str(tmp_path) in captured["argv"]


def test_suggested_git_commands_falls_back_when_branch_detection_fails(
    tmp_path: Path, monkeypatch
):
    """Detached HEAD / non-git dir / git missing must not produce a misleading
    push hint — emit bare `git push` so the user's own tracking config applies."""
    import subprocess as sp

    def fake_run(argv, capture_output=False, text=False, timeout=None, check=False):
        return sp.CompletedProcess(args=argv, returncode=0, stdout="HEAD\n", stderr="")

    monkeypatch.setattr(P.subprocess, "run", fake_run)
    cmds = P.suggested_git_commands(
        Path("docs/blog/posts/x.md"),
        ".blogflow/sessions/abc",
        repo_root=tmp_path,
    )
    assert "git push" in cmds
    # No `origin master` / `origin main` hardcoded.
    assert not any("origin master" in c or "origin main" in c for c in cmds)


def test_validate_post_path_honors_configured_blog_dir(repo_root: Path):
    """Config supports `blog_dir`; path validation must reject/accept based on
    that config value rather than always forcing `docs/blog/posts/`."""
    custom = repo_root / "content" / "blog"
    custom.mkdir(parents=True)
    # Default blog_dir rejects a path under /content/blog
    with pytest.raises(PublishError):
        P.validate_post_path(repo_root, "content/blog/post.md")
    # With blog_dir override, the same path validates cleanly.
    assert P.validate_post_path(
        repo_root, "content/blog/post.md", "content/blog"
    ) == (repo_root / "content/blog/post.md").resolve()


def test_merge_final_respects_update_updated_date_false(sample_post: Path):
    """config.publish.update_updated_date = false used to be a silent no-op;
    now it must actually prevent touching the `date.updated` field."""
    P.merge_final_into_post(
        sample_post,
        "## kept\n",
        today=date(2026, 4, 20),
        ensure_draft_false=True,
        topic="Sample Post",
        author="bnbong",
        update_updated_date=False,
    )
    text = sample_post.read_text(encoding="utf-8")
    # The fixture ships with updated: 2025-01-01 — it must stay put.
    assert "2025-01-01" in text
    assert "2026-04-20" not in text
