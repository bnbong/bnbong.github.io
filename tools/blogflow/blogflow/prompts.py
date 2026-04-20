"""Jinja2 prompt template loader (user override → package default)."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from jinja2 import (
    ChoiceLoader,
    Environment,
    FileSystemLoader,
    PackageLoader,
    StrictUndefined,
)

STAGE_TEMPLATES = {
    "ideas": "ideas.md.j2",
    "brief": "brief.md.j2",
    "draft": "draft.md.j2",
    "review": "review.md.j2",
    "finalize": "finalize.md.j2",
    "reflection": "reflection.md.j2",
}


def _environment(repo_root: Path) -> Environment:
    user_dir = repo_root / ".blogflow" / "prompts"
    loaders = []
    if user_dir.exists():
        loaders.append(FileSystemLoader(str(user_dir)))
    loaders.append(PackageLoader("blogflow", "prompts_tpl"))
    env = Environment(
        loader=ChoiceLoader(loaders),
        autoescape=False,
        undefined=StrictUndefined,
        keep_trailing_newline=True,
    )
    return env


def render(stage: str, context: dict[str, Any], repo_root: Path) -> str:
    if stage not in STAGE_TEMPLATES:
        raise KeyError(f"Unknown prompt stage: {stage}")
    env = _environment(repo_root)
    template = env.get_template(STAGE_TEMPLATES[stage])
    return template.render(**context)
