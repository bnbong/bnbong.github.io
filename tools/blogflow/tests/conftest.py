"""Shared pytest fixtures."""

from __future__ import annotations

from pathlib import Path

import pytest
import yaml


@pytest.fixture
def repo_root(tmp_path: Path) -> Path:
    """A temp directory laid out like the real repo: mkdocs.yml + .blogflow/config.yaml."""
    (tmp_path / "mkdocs.yml").write_text("site_name: test\n", encoding="utf-8")
    blog_dir = tmp_path / "docs" / "blog" / "posts"
    blog_dir.mkdir(parents=True)
    config = {
        "author": "bnbong",
        "blog_dir": "docs/blog/posts",
        "default_category": "Computer Science",
        "claude": {"model": None, "timeout_sec": 10},
        "codex": {
            "model": None,
            "sandbox_review": "read-only",
            "sandbox_exec": "workspace-write",
            "timeout_sec": 10,
        },
        "publish": {"update_updated_date": True, "ensure_draft_false": True},
    }
    blogflow_dir = tmp_path / ".blogflow"
    blogflow_dir.mkdir()
    (blogflow_dir / "config.yaml").write_text(
        yaml.safe_dump(config, sort_keys=False, allow_unicode=True), encoding="utf-8"
    )
    return tmp_path


@pytest.fixture
def sample_post(repo_root: Path) -> Path:
    post = repo_root / "docs" / "blog" / "posts" / "20250101" / "sample.md"
    post.parent.mkdir(parents=True, exist_ok=True)
    post.write_text(
        """---
title: Sample Post
description: A sample post
authors: [bnbong]
date:
  created: 2025-01-01
  updated: 2025-01-01
categories:
  - Test
tags:
  - sample
comments: true
---

Hello, world.
""",
        encoding="utf-8",
    )
    return post
