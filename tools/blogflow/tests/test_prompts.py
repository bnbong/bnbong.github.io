from __future__ import annotations

from pathlib import Path

from blogflow import prompts
from blogflow.models import Brief, BriefQuestion, Draft, Review
from blogflow.state import Session


def _session() -> Session:
    return Session(
        id="sid",
        topic="IPv4",
        slug="ipv4",
        target_post_path="docs/blog/posts/x/x.md",
    )


def _brief() -> Brief:
    return Brief(
        goal="Understand IPv4",
        learning_brief="IPv4 basics",
        source_pack=[{"label": "RFC791", "url": "https://rfc/791", "note": "spec"}],
        scope="in: header; out: v6",
        questions=[BriefQuestion(id="q1", text="Why now?", why="Context")],
        outline=["Intro", "Header"],
        claim_categories=["spec"],
    )


def _draft() -> Draft:
    return Draft(
        title_candidates=["IPv4 Intro"],
        description_candidates=["Learn IPv4 basics."],
        body_markdown="## Intro\n\nHello. [SUPPORTED:RFC791]\n",
        claim_summary=[
            {
                "claim": "IP header is 20 bytes",
                "status": "SUPPORTED",
                "source": "RFC791",
            }
        ],
        references=[{"label": "RFC791", "url": "https://rfc/791"}],
        known_risks=["watch for length"],
    )


def test_ideas_template_renders(repo_root: Path):
    text = prompts.render(
        "ideas",
        {
            "author": "bnbong",
            "default_category": "CS",
            "category": "Network",
            "count": 5,
            "recent_titles": ["A", "B"],
        },
        repo_root,
    )
    assert "bnbong" in text
    assert "Network" in text


def test_brief_template_renders(repo_root: Path):
    text = prompts.render(
        "brief",
        {
            "author": "bnbong",
            "default_category": "CS",
            "session": _session(),
            "recent_titles": [],
        },
        repo_root,
    )
    assert "IPv4" in text
    assert "JSON" in text


def test_draft_template_renders(repo_root: Path):
    text = prompts.render(
        "draft",
        {
            "author": "bnbong",
            "session": _session(),
            "brief": _brief(),
            "answers": {"q1": "Because of IPv4 exhaustion."},
        },
        repo_root,
    )
    assert "IPv4 exhaustion" in text
    assert "RFC791" in text


def test_draft_template_embeds_review_feedback_on_revise_loop(repo_root: Path):
    """When a revise loop feeds the previous review into draft, the template
    must surface it — otherwise the rewrite ignores the reviewer and just
    regenerates the same draft. We intentionally do NOT pass the prior draft
    back to keep revise-loop input tokens bounded."""
    session = _session()
    session.review_gate = "revise"
    text = prompts.render(
        "draft",
        {
            "author": "bnbong",
            "session": session,
            "brief": _brief(),
            "answers": {"q1": "A."},
            "prior_review": "- claim X is unsourced\nGATE: REVISE",
        },
        repo_root,
    )
    assert "Reviewer feedback" in text
    assert "claim X is unsourced" in text
    assert "GATE: REVISE" in text
    assert "Required-fixes" in text or "Required fixes" in text


def test_review_template_biases_toward_approved(repo_root: Path):
    """Reviewer prompt must frame APPROVED as the default outcome, not the
    exception — otherwise the gate always flips to REVISE on stylistic nits."""
    text = prompts.render(
        "review",
        {
            "author": "bnbong",
            "session": _session(),
            "brief": _brief(),
            "draft": _draft(),
        },
        repo_root,
    )
    # default/expected APPROVED wording
    assert "default" in text.lower()
    # non-blocking categories are spelled out
    assert "Suggestions" in text
    # the three blocking categories are named
    assert "Hallucination" in text
    assert "Factually wrong" in text


def test_review_template_includes_gate_instruction(repo_root: Path):
    text = prompts.render(
        "review",
        {
            "author": "bnbong",
            "session": _session(),
            "brief": _brief(),
            "draft": _draft(),
        },
        repo_root,
    )
    assert "GATE: APPROVED" in text
    assert "GATE: REVISE" in text
    assert "GATE: BLOCK" in text


def test_finalize_template_applies_only_required_fixes_and_strips_markers(
    repo_root: Path,
):
    """The finalize template must (a) apply Required-fixes only (mirror the
    draft revise-loop rule so suggestions don't get silently applied) and
    (b) instruct Claude to strip `[SUPPORTED:…]` / `[ASSUMED]` markers so they
    never leak into the published body."""
    review = Review(raw="(review body)", gate="approved")
    text = prompts.render(
        "finalize",
        {
            "author": "bnbong",
            "session": _session(),
            "brief": _brief(),
            "draft": _draft(),
            "review": review,
            "reflection": "",
        },
        repo_root,
    )
    lowered = text.lower()
    # Required-fixes applied; Suggestions ignored.
    assert "required fixes" in lowered
    assert "ignore" in lowered and "suggestions" in lowered
    # Strip provenance markers.
    assert "[SUPPORTED:" in text  # literal marker referenced in instructions
    assert "[ASSUMED]" in text
    assert "strip" in lowered or "remove" in lowered


def test_finalize_template_renders_with_and_without_reflection(repo_root: Path):
    review = Review(raw="review text", gate="approved")
    text_with = prompts.render(
        "finalize",
        {
            "author": "bnbong",
            "session": _session(),
            "brief": _brief(),
            "draft": _draft(),
            "review": review,
            "reflection": "I learned X.",
        },
        repo_root,
    )
    assert "I learned X." in text_with
    assert "회고" in text_with

    text_without = prompts.render(
        "finalize",
        {
            "author": "bnbong",
            "session": _session(),
            "brief": _brief(),
            "draft": _draft(),
            "review": review,
            "reflection": "",
        },
        repo_root,
    )
    assert "skip" in text_without.lower() or "(" in text_without


def test_reflection_template_renders(repo_root: Path):
    text = prompts.render(
        "reflection",
        {"author": "bnbong", "session": _session()},
        repo_root,
    )
    assert "IPv4" in text


def test_user_override_wins(repo_root: Path):
    override_dir = repo_root / ".blogflow" / "prompts"
    override_dir.mkdir(parents=True, exist_ok=True)
    (override_dir / "ideas.md.j2").write_text("OVERRIDE {{ author }}", encoding="utf-8")
    text = prompts.render(
        "ideas",
        {
            "author": "bnbong",
            "default_category": "CS",
            "category": None,
            "count": 3,
            "recent_titles": [],
        },
        repo_root,
    )
    assert text.startswith("OVERRIDE bnbong")
