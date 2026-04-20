"""`blogflow draft` — Claude generates the full draft body + metadata."""

from __future__ import annotations

import json

import click

from .. import prompts, state
from ..errors import AdapterError
from ..models import Brief
from ..schemas import DRAFT_SCHEMA
from . import _context as ctx_mod


@click.command("draft")
@click.option(
    "--session", "session_id", default=None, help="Session id (defaults to latest)."
)
def draft_cmd(session_id: str | None) -> None:
    ctx = ctx_mod.build_context()
    session = ctx.store.resolve_latest(session_id)
    session_dir = ctx.store.session_path(session.id)

    if session.status != state.STATUS_DRAFT_READY:
        raise click.ClickException(
            f"Session must be in {state.STATUS_DRAFT_READY!r}; got {session.status!r}. "
            f"Next: {ctx_mod.next_hint(session.status)}"
        )

    brief = Brief.from_dict(ctx_mod.read_json(session_dir / "outputs" / "brief.json"))
    answers = (
        ctx_mod.read_yaml(session_dir / "user" / "answers.yaml").get("answers") or {}
    )

    # On a revise-loop rerun, feed only the prior review back. We deliberately
    # do NOT include the previous draft: it roughly doubles input tokens for
    # little gain, since review.md already names the sentences to rewrite.
    prior_review = None
    if session.review_gate in {"revise", "block"}:
        review_path = session_dir / "outputs" / "review.md"
        if review_path.exists():
            prior_review = review_path.read_text(encoding="utf-8")

    prompt = prompts.render(
        "draft",
        {
            "author": ctx.author(),
            "session": session,
            "brief": brief,
            "answers": answers,
            "prior_review": prior_review,
        },
        ctx.repo_root,
    )
    ctx_mod.write_prompt(session_dir, "draft", prompt)

    adapter = ctx.claude_adapter()
    result = adapter.run(
        prompt,
        schema=DRAFT_SCHEMA,
        log_dir=session_dir / "logs",
        stage="draft",
    )
    if not result.ok:
        raise AdapterError(
            f"claude draft failed (exit={result.exit_code}). See log under {session_dir / 'logs'}."
        )

    parsed = result.parsed or _loose_parse(result.text)
    if parsed is None:
        raise AdapterError("Could not parse draft JSON. See log.")

    ctx_mod.write_json(session_dir / "outputs" / "draft.json", parsed)
    ctx_mod.write_json(session_dir / "schemas" / "draft.schema.json", DRAFT_SCHEMA)
    (session_dir / "outputs" / "draft.md").write_text(
        parsed.get("body_markdown", ""), encoding="utf-8"
    )
    ctx_mod.write_json(
        session_dir / "outputs" / "draft.claims.json",
        {
            "claim_summary": parsed.get("claim_summary") or [],
            "references": parsed.get("references") or [],
            "known_risks": parsed.get("known_risks") or [],
        },
    )

    state.transition(session, state.STATUS_UNDER_REVIEW)
    ctx.store.save(session)

    click.echo(f"draft → {session_dir / 'outputs' / 'draft.md'}")
    click.echo("Next: blogflow review")


def _loose_parse(text: str) -> dict | None:
    try:
        data = json.loads(text)
    except json.JSONDecodeError:
        return None
    return data if isinstance(data, dict) else None
