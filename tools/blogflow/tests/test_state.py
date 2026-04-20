from __future__ import annotations

from pathlib import Path

import pytest

from blogflow import state as S
from blogflow.errors import StateError


def test_slugify_handles_korean_and_specials():
    assert S.slugify("Hello IPv4 — intro!") == "hello-ipv4-intro"
    assert S.slugify("네트워크 3장") == "네트워크-3장"
    assert S.slugify("  ") == "post"


def test_session_id_format():
    sid = S.new_session_id("IPv4")
    assert "-ipv4" in sid
    assert len(sid.split("-")[0]) == 8  # YYYYMMDD


def test_transition_allowed_and_denied():
    s = S.Session(id="x", topic="x", slug="x")
    S.transition(s, S.STATUS_BRIEF_READY)
    assert s.status == S.STATUS_BRIEF_READY
    S.transition(s, S.STATUS_AWAITING_ANSWERS)
    with pytest.raises(StateError) as exc:
        S.transition(s, S.STATUS_PUBLISHED)
    assert exc.value.expected_command == S.NEXT_COMMAND_HINT[S.STATUS_AWAITING_ANSWERS]


def test_transition_self_is_noop():
    s = S.Session(id="x", topic="x", slug="x", status=S.STATUS_DRAFT_READY)
    S.transition(s, S.STATUS_DRAFT_READY)
    assert s.status == S.STATUS_DRAFT_READY


def test_session_store_roundtrip(tmp_path: Path):
    store = S.SessionStore(tmp_path)
    s = S.Session(
        id="sid", topic="IPv4", slug="ipv4", target_post_path="docs/blog/posts/x.md"
    )
    store.create(s)
    loaded = store.load("sid")
    assert loaded.topic == "IPv4"
    assert loaded.target_post_path == "docs/blog/posts/x.md"
    assert store.list_sessions() == ["sid"]


def test_session_store_resolve_latest(tmp_path: Path):
    store = S.SessionStore(tmp_path)
    s1 = S.Session(id="a", topic="t1", slug="t1", updated_at="2026-04-20T10:00:00")
    s2 = S.Session(id="b", topic="t2", slug="t2", updated_at="2026-04-20T10:00:01")
    store.create(s1)
    store.create(s2)
    # re-save with fixed updated_at since create()/save() overrides updated_at
    s1.updated_at = "2026-04-20T10:00:00"
    store.session_file(s1.id).write_text(
        __import__("yaml").safe_dump(s1.to_dict(), sort_keys=False, allow_unicode=True),
        encoding="utf-8",
    )
    s2.updated_at = "2026-04-20T10:00:05"
    store.session_file(s2.id).write_text(
        __import__("yaml").safe_dump(s2.to_dict(), sort_keys=False, allow_unicode=True),
        encoding="utf-8",
    )
    latest = store.resolve_latest()
    assert latest.id == "b"


def test_find_repo_root_finds_config(repo_root: Path):
    nested = repo_root / "docs" / "deep"
    nested.mkdir(parents=True, exist_ok=True)
    assert S.find_repo_root(nested) == repo_root


def test_next_hint_matches_actual_command_for_each_state():
    """Issue 3: the hint for each state must match the command whose state-gate
    accepts that state. Happy-path users should be able to follow `next: ...`
    without the CLI then refusing with a state-mismatch error."""
    expected = {
        S.STATUS_INITIATED: "blogflow brief",
        S.STATUS_AWAITING_ANSWERS: "blogflow answer",
        S.STATUS_DRAFT_READY: "blogflow draft",
        S.STATUS_UNDER_REVIEW: "blogflow review",
        S.STATUS_AWAITING_REFLECTION: "blogflow reflection",
        S.STATUS_FINAL_READY: "blogflow finalize",
        S.STATUS_APPROVED: "blogflow publish",
    }
    for status, hint in expected.items():
        assert S.NEXT_COMMAND_HINT[status] == hint, f"wrong hint for {status}"


def test_new_session_id_autoincrements_on_collision():
    """Issue 5: same-minute same-topic must not collide."""
    from datetime import datetime

    now = datetime(2026, 4, 20, 10, 30)
    existing = {"20260420-1030-ipv4"}
    sid = S.new_session_id("IPv4", now=now, existing=existing)
    assert sid == "20260420-1030-ipv4-2"

    existing.add("20260420-1030-ipv4-2")
    sid2 = S.new_session_id("IPv4", now=now, existing=existing)
    assert sid2 == "20260420-1030-ipv4-3"


def test_session_store_create_raises_on_duplicate(tmp_path: Path):
    """Issue 5: create() must refuse to silently reuse an existing session dir."""
    store = S.SessionStore(tmp_path)
    s = S.Session(id="dup", topic="t", slug="t")
    store.create(s)
    with pytest.raises(StateError):
        store.create(S.Session(id="dup", topic="t", slug="t"))


def test_session_store_resolve_latest_picks_newer_within_same_second(tmp_path: Path):
    """Two sessions saved in the same wall-clock second used to tie on
    updated_at (seconds precision) and resolve_latest returned whichever came
    first alphabetically. With microsecond precision plus created_at/id
    tie-breakers, the session that was actually saved *later* must win so
    that switching to a new topic does not accidentally reuse the old session.
    """
    store = S.SessionStore(tmp_path)
    s_a = S.Session(id="20260420-2122-ipv4", topic="IPv4", slug="ipv4")
    s_b = S.Session(id="20260420-2122-ipv6", topic="IPv6", slug="ipv6")
    store.create(s_a)
    # store.save() writes the real, current timestamp — so creating s_b after
    # s_a guarantees s_b.updated_at > s_a.updated_at at microsecond precision.
    store.create(s_b)
    assert store.resolve_latest().id == s_b.id

    # Flip the creation order: the session created second must still win.
    tmp_path_2 = tmp_path / "alt"
    tmp_path_2.mkdir()
    store2 = S.SessionStore(tmp_path_2)
    t_b = S.Session(id="20260420-2122-ipv6", topic="IPv6", slug="ipv6")
    t_a = S.Session(id="20260420-2122-ipv4", topic="IPv4", slug="ipv4")
    store2.create(t_b)
    store2.create(t_a)
    assert store2.resolve_latest().id == t_a.id


def test_session_store_resolve_latest_tiebreak_on_identical_timestamps(tmp_path: Path):
    """Belt-and-suspenders: if even microsecond updated_at somehow ties, the
    tie-breaker on created_at (and then id) keeps the selection deterministic."""
    store = S.SessionStore(tmp_path)
    s1 = S.Session(
        id="20260420-2122-a",
        topic="a",
        slug="a",
        created_at="2026-04-20T21:22:00.000100",
        updated_at="2026-04-20T21:22:30.555555",
    )
    s2 = S.Session(
        id="20260420-2122-b",
        topic="b",
        slug="b",
        created_at="2026-04-20T21:22:00.000500",
        updated_at="2026-04-20T21:22:30.555555",
    )
    store.create(s1)
    store.create(s2)
    import yaml as _yaml

    # Overwrite updated_at after create() so they genuinely tie.
    for s in (s1, s2):
        store.session_file(s.id).write_text(
            _yaml.safe_dump(s.to_dict(), sort_keys=False, allow_unicode=True),
            encoding="utf-8",
        )
    # s2 has later created_at, so it must win.
    assert store.resolve_latest().id == s2.id
