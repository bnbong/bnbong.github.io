"""Typed dataclasses for session artifacts."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date
from typing import Any


@dataclass
class BriefQuestion:
    id: str
    text: str
    why: str = ""


@dataclass
class Brief:
    goal: str
    learning_brief: str
    source_pack: list[dict[str, str]] = field(default_factory=list)
    scope: str = ""
    questions: list[BriefQuestion] = field(default_factory=list)
    outline: list[str] = field(default_factory=list)
    claim_categories: list[str] = field(default_factory=list)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "Brief":
        qs = [
            BriefQuestion(
                id=str(q.get("id", f"q{i + 1}")),
                text=q.get("text", ""),
                why=q.get("why", ""),
            )
            for i, q in enumerate(data.get("questions") or [])
        ]
        return cls(
            goal=data.get("goal", ""),
            learning_brief=data.get("learning_brief", ""),
            source_pack=list(data.get("source_pack") or []),
            scope=data.get("scope", ""),
            questions=qs,
            outline=list(data.get("outline") or []),
            claim_categories=list(data.get("claim_categories") or []),
        )


@dataclass
class Draft:
    title_candidates: list[str]
    description_candidates: list[str]
    body_markdown: str
    claim_summary: list[dict[str, str]] = field(default_factory=list)
    references: list[dict[str, str]] = field(default_factory=list)
    known_risks: list[str] = field(default_factory=list)


@dataclass
class Review:
    raw: str
    gate: str  # "approved" | "revise" | "block" | "unclear"
    findings: list[str] = field(default_factory=list)


@dataclass
class Frontmatter:
    raw: dict[str, Any]
    body: str

    def ensure_published(self, *, today: date, ensure_draft_false: bool) -> None:
        if "date" not in self.raw or not isinstance(self.raw["date"], dict):
            self.raw["date"] = {
                "created": today.isoformat(),
                "updated": today.isoformat(),
            }
        else:
            self.raw["date"].setdefault("created", today.isoformat())
            self.raw["date"]["updated"] = today.isoformat()
        if ensure_draft_false and self.raw.get("draft") is True:
            self.raw["draft"] = False
