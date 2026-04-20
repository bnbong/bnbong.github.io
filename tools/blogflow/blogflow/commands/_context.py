"""Shared helpers: repo/config/session/adapter wiring for command handlers."""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml

from ..adapters.claude import ClaudeAdapter
from ..adapters.codex import CodexAdapter
from ..errors import ConfigError
from ..state import (
    NEXT_COMMAND_HINT,
    Session,
    SessionStore,
    find_repo_root,
    load_config,
)


@dataclass
class Context:
    repo_root: Path
    config: dict[str, Any]
    store: SessionStore

    def recent_post_titles(self, limit: int = 10) -> list[str]:
        blog_dir = self.repo_root / self.config.get("blog_dir", "docs/blog/posts")
        if not blog_dir.exists():
            return []
        titles: list[str] = []
        for md in sorted(blog_dir.rglob("*.md"), reverse=True):
            try:
                text = md.read_text(encoding="utf-8")
            except OSError:
                continue
            if not text.startswith("---"):
                continue
            try:
                parts = text.split("---", 2)
                meta = yaml.safe_load(parts[1]) or {}
            except Exception:
                continue
            t = meta.get("title")
            if isinstance(t, str):
                titles.append(t)
            if len(titles) >= limit:
                break
        return titles

    def author(self) -> str:
        return str(self.config.get("author", "author"))

    def default_category(self) -> str:
        return str(self.config.get("default_category", "General"))

    def claude_adapter(self) -> ClaudeAdapter:
        cfg = self.config.get("claude") or {}
        return ClaudeAdapter(
            model=cfg.get("model"),
            timeout_sec=_optional_timeout(cfg.get("timeout_sec")),
        )

    def codex_adapter(self) -> CodexAdapter:
        cfg = self.config.get("codex") or {}
        adapter = CodexAdapter(
            model=cfg.get("model"),
            sandbox_exec=str(cfg.get("sandbox_exec", "workspace-write")),
            sandbox_review=str(cfg.get("sandbox_review", "read-only")),
            timeout_sec=_optional_timeout(cfg.get("timeout_sec")),
        )
        if "reasoning_effort" in cfg:
            effort = cfg.get("reasoning_effort")
            adapter.reasoning_effort = None if effort in (None, "") else str(effort)
        return adapter


def build_context(start: Path | None = None) -> Context:
    repo_root = find_repo_root(start)
    config = _load_config_or_default(repo_root)
    store = SessionStore(repo_root)
    return Context(repo_root=repo_root, config=config, store=store)


def _load_config_or_default(repo_root: Path) -> dict[str, Any]:
    try:
        return load_config(repo_root)
    except ConfigError:
        return {
            "author": "author",
            "blog_dir": "docs/blog/posts",
            "default_category": "General",
            "claude": {"timeout_sec": None},
            "codex": {
                "sandbox_review": "read-only",
                "sandbox_exec": "workspace-write",
                "timeout_sec": None,
            },
            "publish": {"update_updated_date": True, "ensure_draft_false": True},
        }


def _optional_timeout(value: Any) -> int | None:
    """Config may supply ``null``, 0, missing — all mean "no timeout"."""
    if value in (None, "", 0, "0"):
        return None
    return int(value)


def session_rel_path(ctx: Context, session: Session) -> str:
    return f".blogflow/sessions/{session.id}"


def write_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")


def write_yaml(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        yaml.safe_dump(data, sort_keys=False, allow_unicode=True),
        encoding="utf-8",
    )


def read_yaml(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    if not isinstance(data, dict):
        raise ConfigError(f"{path} must be a YAML mapping.")
    return data


def read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def next_hint(status: str) -> str:
    return NEXT_COMMAND_HINT.get(status, "(unknown)")


def write_prompt(session_dir: Path, stage: str, prompt: str) -> Path:
    out = session_dir / "prompts" / f"{stage}.txt"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(prompt, encoding="utf-8")
    return out
