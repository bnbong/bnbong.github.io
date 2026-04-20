"""JSON Schema constants used with `claude --json-schema`."""

from __future__ import annotations

IDEAS_SCHEMA: dict = {
    "type": "object",
    "required": ["ideas"],
    "additionalProperties": False,
    "properties": {
        "ideas": {
            "type": "array",
            "minItems": 1,
            "items": {
                "type": "object",
                "required": ["title", "why_now", "audience", "difficulty"],
                "additionalProperties": True,
                "properties": {
                    "title": {"type": "string"},
                    "why_now": {"type": "string"},
                    "audience": {"type": "string"},
                    "difficulty": {"type": "string"},
                    "source_requirements": {"type": "string"},
                    "hallucination_risk": {"type": "string"},
                    "single_or_series": {"type": "string"},
                },
            },
        }
    },
}

BRIEF_SCHEMA: dict = {
    "type": "object",
    "required": ["goal", "learning_brief", "questions", "outline"],
    "additionalProperties": True,
    "properties": {
        "goal": {"type": "string"},
        "learning_brief": {"type": "string"},
        "source_pack": {
            "type": "array",
            "items": {
                "type": "object",
                "required": ["label"],
                "properties": {
                    "label": {"type": "string"},
                    "url": {"type": "string"},
                    "note": {"type": "string"},
                },
            },
        },
        "scope": {"type": "string"},
        "questions": {
            "type": "array",
            "minItems": 1,
            "items": {
                "type": "object",
                "required": ["id", "text"],
                "properties": {
                    "id": {"type": "string"},
                    "text": {"type": "string"},
                    "why": {"type": "string"},
                },
            },
        },
        "outline": {"type": "array", "items": {"type": "string"}},
        "claim_categories": {"type": "array", "items": {"type": "string"}},
    },
}

DRAFT_SCHEMA: dict = {
    "type": "object",
    "required": ["title_candidates", "description_candidates", "body_markdown"],
    "additionalProperties": True,
    "properties": {
        "title_candidates": {
            "type": "array",
            "items": {"type": "string"},
            "minItems": 1,
        },
        "description_candidates": {
            "type": "array",
            "items": {"type": "string"},
            "minItems": 1,
        },
        "body_markdown": {"type": "string", "minLength": 1},
        "claim_summary": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "claim": {"type": "string"},
                    "status": {"type": "string"},
                    "source": {"type": "string"},
                },
            },
        },
        "references": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "label": {"type": "string"},
                    "url": {"type": "string"},
                },
            },
        },
        "known_risks": {"type": "array", "items": {"type": "string"}},
    },
}

SCHEMA_REGISTRY: dict[str, dict] = {
    "ideas": IDEAS_SCHEMA,
    "brief": BRIEF_SCHEMA,
    "draft": DRAFT_SCHEMA,
}


def get(name: str) -> dict:
    return SCHEMA_REGISTRY[name]
