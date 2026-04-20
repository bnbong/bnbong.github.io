from __future__ import annotations

from datetime import date
from pathlib import Path

import pytest

from blogflow import frontmatter as fm_mod
from blogflow.errors import PublishError
from blogflow.models import Frontmatter


def test_parse_and_dump_roundtrip(sample_post: Path):
    fm = fm_mod.read(sample_post)
    assert fm.raw["title"] == "Sample Post"
    assert fm.body.startswith("Hello, world.")
    dumped = fm_mod.dump(fm)
    assert dumped.startswith("---\n")
    assert "title: Sample Post" in dumped
    assert "Hello, world." in dumped


def test_ensure_published_updates_dates_only():
    fm = Frontmatter(
        raw={"date": {"created": "2025-01-01", "updated": "2025-01-01"}},
        body="",
    )
    fm.ensure_published(today=date(2026, 4, 20), ensure_draft_false=True)
    assert fm.raw["date"]["created"] == "2025-01-01"
    assert fm.raw["date"]["updated"] == "2026-04-20"
    assert "draft" not in fm.raw


def test_ensure_published_flips_only_when_draft_true():
    fm = Frontmatter(raw={"draft": True}, body="")
    fm.ensure_published(today=date(2026, 4, 20), ensure_draft_false=True)
    assert fm.raw["draft"] is False


def test_ensure_published_leaves_date_created_when_missing():
    fm = Frontmatter(raw={}, body="")
    fm.ensure_published(today=date(2026, 4, 20), ensure_draft_false=True)
    assert fm.raw["date"]["created"] == "2026-04-20"
    assert fm.raw["date"]["updated"] == "2026-04-20"


def test_parse_rejects_unclosed_fence():
    with pytest.raises(PublishError):
        fm_mod.parse("---\ntitle: x\nbody without fence")


def test_write_atomic_overwrites(tmp_path: Path):
    path = tmp_path / "p.md"
    path.write_text("---\ntitle: old\n---\n\nbody\n", encoding="utf-8")
    fm = fm_mod.read(path)
    fm.raw["title"] = "new"
    fm_mod.write_atomic(path, fm)
    assert "title: new" in path.read_text(encoding="utf-8")


def test_dump_preserves_key_order():
    fm = Frontmatter(
        raw={"title": "t", "date": {"created": "2025-01-01"}, "tags": ["a"]},
        body="body\n",
    )
    text = fm_mod.dump(fm)
    title_pos = text.find("title:")
    date_pos = text.find("date:")
    tags_pos = text.find("tags:")
    assert 0 <= title_pos < date_pos < tags_pos
