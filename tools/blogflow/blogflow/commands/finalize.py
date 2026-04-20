"""`blogflow finalize` — merge draft/review/reflection into a final body."""

from __future__ import annotations

import re

import click

from .. import prompts, state
from ..errors import AdapterError
from ..models import Brief, Draft, Review
from . import _context as ctx_mod

# Match `[SUPPORTED:<label>]` (any non-`]` content inside) and bare `[ASSUMED]`.
# The optional leading whitespace eats the space between prose and the marker
# so `"header is 20 bytes [SUPPORTED:RFC 791]."` → `"header is 20 bytes."`.
_PROVENANCE_MARKER_RE = re.compile(
    r"[ \t]*\[(?:SUPPORTED:[^\]]+|ASSUMED)\]",
    re.IGNORECASE,
)


def strip_provenance_markers(text: str) -> str:
    """Remove `[SUPPORTED:<label>]` and `[ASSUMED]` tags from rendered prose.

    Draft/review stages rely on these markers for provenance auditing, but
    they must never reach the public post body — they look like unfinished
    annotations to readers.
    """
    return _PROVENANCE_MARKER_RE.sub("", text)


@click.command("finalize")
@click.option(
    "--session", "session_id", default=None, help="Session id (defaults to latest)."
)
@click.option(
    "--deterministic",
    is_flag=True,
    default=False,
    help=(
        "Skip the Claude polish pass and concatenate draft + reflection as-is. "
        "Use this only when the review has no Required-fixes to apply; otherwise "
        "review feedback is silently dropped."
    ),
)
def finalize_cmd(session_id: str | None, deterministic: bool) -> None:
    ctx = ctx_mod.build_context()
    session = ctx.store.resolve_latest(session_id)
    session_dir = ctx.store.session_path(session.id)

    if session.status != state.STATUS_FINAL_READY:
        raise click.ClickException(
            f"Session must be in {state.STATUS_FINAL_READY!r}; got {session.status!r}. "
            f"Next: {ctx_mod.next_hint(session.status)}"
        )

    brief = Brief.from_dict(ctx_mod.read_json(session_dir / "outputs" / "brief.json"))
    draft_data = ctx_mod.read_json(session_dir / "outputs" / "draft.json")
    draft = Draft(
        title_candidates=list(draft_data.get("title_candidates") or []),
        description_candidates=list(draft_data.get("description_candidates") or []),
        body_markdown=draft_data.get("body_markdown", ""),
        claim_summary=list(draft_data.get("claim_summary") or []),
        references=list(draft_data.get("references") or []),
        known_risks=list(draft_data.get("known_risks") or []),
    )
    review_path = session_dir / "outputs" / "review.md"
    review_raw = review_path.read_text(encoding="utf-8") if review_path.exists() else ""
    review = Review(raw=review_raw, gate=(session.review_gate or "approved"))
    reflection_path = session_dir / "user" / "reflection.md"
    reflection_text = (
        reflection_path.read_text(encoding="utf-8").strip()
        if reflection_path.exists() and not session.reflection_skipped
        else ""
    )

    has_review_body = bool(review_raw.strip())

    if deterministic:
        # Explicit opt-out: warn if we're about to ignore non-trivial review content.
        if has_review_body and not _review_is_trivially_approved(review_raw):
            click.echo(
                "warning: --deterministic skips Claude polish. The review may "
                "have Required-fixes that will NOT be applied to final.md."
            )
            click.echo("         Run without --deterministic to merge them.")
        final_body = _deterministic_merge(draft, reflection_text)
    else:
        # Default path: polish via Claude so review Required-fixes are applied
        # and internal provenance markers are stripped from the prose.
        final_body = _regenerate_via_claude(
            ctx, session, session_dir, brief, draft, review, reflection_text
        )

    # Safety net: strip any provenance markers that survived the finalize
    # stage (happens when --deterministic is used, and defends against the
    # regenerate prompt being ignored by Claude).
    final_body = strip_provenance_markers(final_body)

    (session_dir / "outputs" / "final.md").write_text(final_body, encoding="utf-8")

    state.transition(session, state.STATUS_FINAL_READY)  # idempotent no-op
    ctx.store.save(session)
    click.echo(f"final → {session_dir / 'outputs' / 'final.md'}")
    click.echo("Next: blogflow approve")


def _deterministic_merge(draft: Draft, reflection_text: str) -> str:
    body = draft.body_markdown.rstrip() + "\n"
    if reflection_text:
        body += "\n## 회고\n\n" + reflection_text.strip() + "\n"
    return body


def _review_is_trivially_approved(review_raw: str) -> bool:
    """Best-effort check: review body declares `Required fixes: None`.

    Used only to decide whether --deterministic deserves a warning. False
    positives just produce a spurious warning; false negatives mean the user
    misses one. Neither changes behavior — it's a UX hint.
    """
    # Look for the "Required fixes" heading followed by a "None" line within a
    # handful of lines. The reviewer template emits "> None — draft is …" but
    # freeform reviews may phrase it differently.
    m = re.search(r"required\s+fixes[^\n]*\n+([\s\S]{0,200})", review_raw, re.IGNORECASE)
    if not m:
        return False
    snippet = m.group(1).lower()
    return bool(re.search(r"\bnone\b", snippet))


def _regenerate_via_claude(
    ctx,
    session,
    session_dir,
    brief,
    draft,
    review,
    reflection_text,
) -> str:
    prompt = prompts.render(
        "finalize",
        {
            "author": ctx.author(),
            "session": session,
            "brief": brief,
            "draft": draft,
            "review": review,
            "reflection": reflection_text,
        },
        ctx.repo_root,
    )
    ctx_mod.write_prompt(session_dir, "finalize", prompt)
    adapter = ctx.claude_adapter()
    result = adapter.run(
        prompt,
        schema=None,
        log_dir=session_dir / "logs",
        stage="finalize",
    )
    if not result.ok or not result.text.strip():
        raise AdapterError(
            f"claude finalize failed (exit={result.exit_code}). See log under {session_dir / 'logs'}."
        )
    return result.text.strip() + "\n"
