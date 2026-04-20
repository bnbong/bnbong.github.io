"""`blogflow ideas` — generate topic candidates."""

from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path

import click

from .. import prompts
from ..errors import AdapterError
from ..schemas import IDEAS_SCHEMA
from . import _context as ctx_mod


@click.command("ideas")
@click.option("--category", default=None, help="Focus category for the brainstorm.")
@click.option("--count", default=5, type=int, help="How many ideas to request.")
def ideas_cmd(category: str | None, count: int) -> None:
    """Ask Claude for fresh blog post ideas and save them under `.blogflow/ideas/`."""
    ctx = ctx_mod.build_context()
    prompt_context = {
        "author": ctx.author(),
        "default_category": ctx.default_category(),
        "category": category,
        "count": count,
        "recent_titles": ctx.recent_post_titles(),
    }
    prompt = prompts.render("ideas", prompt_context, ctx.repo_root)

    ideas_dir = ctx.repo_root / ".blogflow" / "ideas"
    ideas_dir.mkdir(parents=True, exist_ok=True)
    ts = datetime.now().strftime("%Y%m%d-%H%M%S")
    log_dir = ideas_dir / "logs"

    adapter = ctx.claude_adapter()
    result = adapter.run(
        prompt,
        schema=IDEAS_SCHEMA,
        log_dir=log_dir,
        stage="ideas",
    )
    if not result.ok:
        raise AdapterError(
            f"claude ideas failed (exit={result.exit_code}). See log at {log_dir}."
        )

    payload = result.parsed or _try_parse(result.text)
    if payload is None:
        raise AdapterError(
            "Could not parse ideas response as JSON. Raw text saved in log."
        )

    out_path = ideas_dir / f"{ts}.yaml"
    _write_ideas(out_path, payload)
    click.echo(f"Saved {len(payload.get('ideas', []))} ideas → {out_path}")
    click.echo('Next: pick one and run `blogflow init --topic "..."`.')


def _try_parse(text: str) -> dict | None:
    try:
        data = json.loads(text)
    except json.JSONDecodeError:
        return None
    return data if isinstance(data, dict) else None


def _write_ideas(path: Path, payload: dict) -> None:
    import yaml

    path.write_text(
        yaml.safe_dump(payload, sort_keys=False, allow_unicode=True),
        encoding="utf-8",
    )
