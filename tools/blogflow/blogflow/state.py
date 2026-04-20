"""Session state and workflow state-machine."""

from __future__ import annotations

import os
import re
import tempfile
from dataclasses import asdict, dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Any

import yaml

from .errors import ConfigError, SessionNotFoundError, StateError

STATUS_INITIATED = "initiated"
STATUS_BRIEF_READY = "brief_ready"
STATUS_AWAITING_ANSWERS = "awaiting_answers"
STATUS_DRAFT_READY = "draft_ready"
STATUS_UNDER_REVIEW = "under_review"
STATUS_AWAITING_REFLECTION = "awaiting_reflection"
STATUS_FINAL_READY = "final_ready"
STATUS_APPROVED = "approved"
STATUS_PUBLISHED = "published"

ALLOWED_TRANSITIONS: dict[str, set[str]] = {
    STATUS_INITIATED: {STATUS_BRIEF_READY},
    STATUS_BRIEF_READY: {STATUS_AWAITING_ANSWERS},
    STATUS_AWAITING_ANSWERS: {STATUS_DRAFT_READY},
    STATUS_DRAFT_READY: {STATUS_UNDER_REVIEW},
    STATUS_UNDER_REVIEW: {STATUS_AWAITING_REFLECTION, STATUS_DRAFT_READY},
    STATUS_AWAITING_REFLECTION: {STATUS_FINAL_READY},
    STATUS_FINAL_READY: {STATUS_APPROVED},
    STATUS_APPROVED: {STATUS_PUBLISHED},
    STATUS_PUBLISHED: set(),
}

NEXT_COMMAND_HINT: dict[str, str] = {
    STATUS_INITIATED: "blogflow brief",
    STATUS_BRIEF_READY: "blogflow answer",
    STATUS_AWAITING_ANSWERS: "blogflow answer",
    STATUS_DRAFT_READY: "blogflow draft",
    STATUS_UNDER_REVIEW: "blogflow review",
    STATUS_AWAITING_REFLECTION: "blogflow reflection",
    STATUS_FINAL_READY: "blogflow finalize",
    STATUS_APPROVED: "blogflow publish",
    STATUS_PUBLISHED: "(workflow complete)",
}


SLUG_RE = re.compile(r"[^a-zA-Z0-9가-힣\-]+")


def slugify(topic: str) -> str:
    slug = SLUG_RE.sub("-", topic.strip().lower()).strip("-")
    return slug[:60] or "post"


def new_session_id(
    topic: str,
    *,
    now: datetime | None = None,
    existing: set[str] | list[str] | None = None,
) -> str:
    """Build a session id. If ``existing`` is supplied and the base id collides,
    append ``-2``, ``-3``, ... until a unique id is produced."""
    now = now or datetime.now()
    base = f"{now.strftime('%Y%m%d-%H%M')}-{slugify(topic)}"
    if not existing:
        return base
    taken = set(existing)
    if base not in taken:
        return base
    n = 2
    while f"{base}-{n}" in taken:
        n += 1
    return f"{base}-{n}"


@dataclass
class Session:
    id: str
    topic: str
    slug: str
    status: str = STATUS_INITIATED
    target_post_path: str | None = None
    # Microsecond precision — seconds-only timestamps collided when two sessions
    # were saved in the same wall-clock second and resolve_latest() then picked
    # the wrong one. Legacy sessions with seconds-only strings still sort
    # correctly against newer microsecond strings (microsecond strings compare
    # greater under lexicographic ordering).
    created_at: str = field(default_factory=lambda: datetime.now().isoformat())
    updated_at: str = field(default_factory=lambda: datetime.now().isoformat())
    approved_at: str | None = None
    published_at: str | None = None
    review_gate: str | None = None
    reflection_skipped: bool = False
    # Count of auto revise-loops taken so far. Incremented each time a Codex
    # review returns REVISE/BLOCK and the session loops back to draft_ready.
    # After MAX_AUTO_REVISE the loop stops auto-transitioning; the author must
    # manually decide with `blogflow review --gate ...`.
    revise_count: int = 0

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "Session":
        known = {f for f in cls.__dataclass_fields__}
        filtered = {k: v for k, v in data.items() if k in known}
        return cls(**filtered)


def transition(session: Session, target: str) -> None:
    """Mutate `session.status` after verifying the transition is legal."""
    current = session.status
    if target == current:
        return
    allowed = ALLOWED_TRANSITIONS.get(current, set())
    if target not in allowed:
        hint = NEXT_COMMAND_HINT.get(current)
        raise StateError(
            f"Illegal transition {current!r} → {target!r}. "
            f"Next expected step for state {current!r}: {hint}",
            expected_command=hint,
        )
    session.status = target
    session.updated_at = datetime.now().isoformat()


class SessionStore:
    """Filesystem-backed session store under .blogflow/sessions/."""

    def __init__(self, root: Path):
        self.root = Path(root)

    def sessions_dir(self) -> Path:
        return self.root / ".blogflow" / "sessions"

    def session_path(self, session_id: str) -> Path:
        return self.sessions_dir() / session_id

    def session_file(self, session_id: str) -> Path:
        return self.session_path(session_id) / "session.yaml"

    def list_sessions(self) -> list[str]:
        d = self.sessions_dir()
        if not d.exists():
            return []
        return sorted(p.name for p in d.iterdir() if p.is_dir())

    def create(self, session: Session) -> Path:
        path = self.session_path(session.id)
        if self.session_file(session.id).exists():
            raise StateError(
                f"Session id {session.id!r} already exists at {path}. "
                f"Re-run `blogflow init` (a suffix will be appended) or pick a different topic."
            )
        for sub in ("prompts", "outputs", "user", "schemas", "logs"):
            (path / sub).mkdir(parents=True, exist_ok=True)
        self.save(session)
        return path

    def load(self, session_id: str) -> Session:
        f = self.session_file(session_id)
        if not f.exists():
            raise SessionNotFoundError(f"No session found: {session_id}")
        data = yaml.safe_load(f.read_text(encoding="utf-8")) or {}
        return Session.from_dict(data)

    def save(self, session: Session) -> None:
        session.updated_at = datetime.now().isoformat()
        f = self.session_file(session.id)
        f.parent.mkdir(parents=True, exist_ok=True)
        text = yaml.safe_dump(session.to_dict(), sort_keys=False, allow_unicode=True)
        _atomic_write(f, text)

    def resolve_latest(self, explicit: str | None = None) -> Session:
        if explicit:
            return self.load(explicit)
        ids = self.list_sessions()
        if not ids:
            raise SessionNotFoundError(
                'No sessions found. Start one with `blogflow init --topic "..."`.'
            )
        candidates = []
        for sid in ids:
            try:
                s = self.load(sid)
                candidates.append(s)
            except SessionNotFoundError:
                continue
        if not candidates:
            raise SessionNotFoundError("No valid sessions.")
        # Tie-break on created_at, then id (lexicographic on minute-precision id
        # is still better than nothing). Without tie-breakers, two sessions
        # saved in the same second (common when you init B right after A's last
        # transition) compared equal and Python's stable sort returned
        # whichever happened to be listed first.
        candidates.sort(
            key=lambda s: (s.updated_at, s.created_at, s.id),
            reverse=True,
        )
        return candidates[0]


def load_config(repo_root: Path) -> dict[str, Any]:
    path = repo_root / ".blogflow" / "config.yaml"
    if not path.exists():
        raise ConfigError(
            f".blogflow/config.yaml not found under {repo_root}. "
            "Run blogflow from the repo root."
        )
    data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    if not isinstance(data, dict):
        raise ConfigError(".blogflow/config.yaml must be a YAML mapping.")
    return data


def find_repo_root(start: Path | None = None) -> Path:
    """Walk up from `start` looking for `.blogflow/config.yaml` or `mkdocs.yml`."""
    cur = (start or Path.cwd()).resolve()
    for parent in [cur, *cur.parents]:
        if (parent / ".blogflow" / "config.yaml").exists():
            return parent
        if (parent / "mkdocs.yml").exists():
            return parent
    raise ConfigError(
        "Could not locate repo root (no .blogflow/config.yaml or mkdocs.yml found in parents)."
    )


def _atomic_write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp = tempfile.mkstemp(prefix=path.name + ".", dir=str(path.parent))
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            f.write(text)
        os.replace(tmp, path)
    except Exception:
        try:
            os.unlink(tmp)
        except FileNotFoundError:
            pass
        raise
