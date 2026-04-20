"""`blogflow review` — Codex reviews the draft and emits a GATE decision."""

from __future__ import annotations

import click

from .. import prompts, state
from ..adapters.codex import (
    GATE_APPROVED,
    GATE_BLOCK,
    GATE_REVISE,
    GATE_UNCLEAR,
    parse_gate,
)
from ..errors import AdapterError
from ..models import Brief, Draft
from . import _context as ctx_mod


_GATE_TO_STATE = {
    GATE_APPROVED: state.STATUS_AWAITING_REFLECTION,
    GATE_REVISE: state.STATUS_DRAFT_READY,
    GATE_BLOCK: state.STATUS_DRAFT_READY,
}

# After this many automatic revise-loops, the review command stops transitioning
# on REVISE/BLOCK and forces the author to decide manually. Without this cap,
# the reviewer and author can spin indefinitely on non-blocking nits.
MAX_AUTO_REVISE = 1


@click.command("review")
@click.option(
    "--session", "session_id", default=None, help="Session id (defaults to latest)."
)
@click.option(
    "--gate",
    "manual_gate",
    type=click.Choice(["approved", "revise", "block"], case_sensitive=False),
    default=None,
    help=(
        "Skip the Codex invocation and apply a manual gate decision. "
        "Use this to resolve an UNCLEAR review or to override what Codex produced."
    ),
)
def review_cmd(session_id: str | None, manual_gate: str | None) -> None:
    ctx = ctx_mod.build_context()
    session = ctx.store.resolve_latest(session_id)
    session_dir = ctx.store.session_path(session.id)

    if session.status != state.STATUS_UNDER_REVIEW:
        raise click.ClickException(
            f"Session must be in {state.STATUS_UNDER_REVIEW!r}; got {session.status!r}. "
            f"Next: {ctx_mod.next_hint(session.status)}"
        )

    if manual_gate is not None:
        _apply_manual_gate(ctx, session, session_dir, manual_gate.upper())
        return

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

    prompt = prompts.render(
        "review",
        {"author": ctx.author(), "session": session, "brief": brief, "draft": draft},
        ctx.repo_root,
    )
    ctx_mod.write_prompt(session_dir, "review", prompt)

    adapter = ctx.codex_adapter()
    result = adapter.run(
        prompt,
        log_dir=session_dir / "logs",
        stage="review",
        extra={"mode": "review"},
    )
    if not result.ok:
        raise AdapterError(
            f"codex review failed (exit={result.exit_code}). See log under {session_dir / 'logs'}."
        )

    (session_dir / "outputs" / "review.md").write_text(result.text, encoding="utf-8")
    gate = parse_gate(result.text)
    _persist_gate_and_transition(ctx, session, session_dir, gate)


def _apply_manual_gate(ctx, session, session_dir, gate_upper: str) -> None:
    """Skip Codex; record the gate and transition the session."""
    review_path = session_dir / "outputs" / "review.md"
    if not review_path.exists():
        review_path.parent.mkdir(parents=True, exist_ok=True)
        review_path.write_text(
            f"(no codex review captured — gate manually set to {gate_upper.lower()})\n",
            encoding="utf-8",
        )
    _persist_gate_and_transition(ctx, session, session_dir, gate_upper, manual=True)


def _persist_gate_and_transition(
    ctx,
    session,
    session_dir,
    gate_upper: str,
    *,
    manual: bool = False,
) -> None:
    meta: dict = {"gate": gate_upper.lower()}
    if manual:
        meta["manual"] = True
    ctx_mod.write_yaml(session_dir / "outputs" / "review.meta.yaml", meta)
    session.review_gate = gate_upper.lower()

    label = "manual" if manual else "codex"
    review_out = session_dir / "outputs" / "review.md"

    # Auto loop cap: once we've already done MAX_AUTO_REVISE automatic revise
    # cycles, do not auto-transition on REVISE/BLOCK. Make the author look at
    # the review and decide — most late-cycle flags are non-blocking nits.
    if (
        not manual
        and gate_upper in {GATE_REVISE, GATE_BLOCK}
        and session.revise_count >= MAX_AUTO_REVISE
    ):
        ctx.store.save(session)
        click.echo(f"review → {review_out}")
        click.echo(
            f"gate ({label}): {gate_upper} — but this session already ran "
            f"{session.revise_count} revise cycle(s)."
        )
        click.echo(
            "Auto-loop stopped to avoid burning tokens on non-blocking nits. "
            "Read the review and pick:"
        )
        click.echo("  blogflow review --gate approved   # ship it")
        click.echo("  blogflow review --gate revise     # one more draft pass")
        click.echo("  blogflow review --gate block      # one more draft pass")
        return

    if gate_upper in _GATE_TO_STATE:
        # Increment only on an auto (codex-emitted) REVISE/BLOCK — manual gate
        # overrides don't count against the loop cap.
        if not manual and gate_upper in {GATE_REVISE, GATE_BLOCK}:
            session.revise_count += 1
        state.transition(session, _GATE_TO_STATE[gate_upper])
        ctx.store.save(session)
        click.echo(f"review → {review_out}")
        click.echo(f"gate ({label}): {gate_upper}")
        click.echo(f"Next: {ctx_mod.next_hint(session.status)}")
        return

    # Unclear — persist and prompt author for manual resolution.
    ctx.store.save(session)
    click.echo(f"review → {review_out}")
    click.echo(f"gate ({label}): {GATE_UNCLEAR} — Codex did not emit a `GATE:` line.")
    click.echo("Resolve by re-running with a manual decision:")
    click.echo("  blogflow review --gate approved   # send to reflection")
    click.echo("  blogflow review --gate revise     # loop back to draft")
    click.echo("  blogflow review --gate block      # loop back to draft")
