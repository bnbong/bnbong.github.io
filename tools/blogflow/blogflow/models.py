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

    def ensure_published(
        self,
        *,
        today: date,
        ensure_draft_false: bool,
        update_updated_date: bool = True,
    ) -> None:
        # Store as `datetime.date`, not an ISO string — mkdocs-material's blog
        # plugin rejects string dates (`Expected type: <class 'datetime.date'>
        # ... but received: <class 'str'>`) and the CI build aborts. PyYAML
        # serializes `date` objects as unquoted `YYYY-MM-DD`, which is exactly
        # the shape the plugin and the rest of the existing posts use.
        if "date" not in self.raw or not isinstance(self.raw["date"], dict):
            # Brand-new frontmatter: set both created and updated regardless
            # of update_updated_date, since the file didn't have an `updated`
            # field to preserve.
            self.raw["date"] = {
                "created": today,
                "updated": today,
            }
        else:
            self.raw["date"].setdefault("created", today)
            if update_updated_date:
                self.raw["date"]["updated"] = today
            else:
                # Preserve whatever `updated` the author set manually, but
                # still seed one if it's missing so the post is valid.
                self.raw["date"].setdefault("updated", today)
        if ensure_draft_false and self.raw.get("draft") is True:
            self.raw["draft"] = False
