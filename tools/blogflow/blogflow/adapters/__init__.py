"""LLM adapters (Claude / Codex)."""

from .base import AdapterResult, LLMAdapter
from .claude import ClaudeAdapter
from .codex import CodexAdapter

__all__ = ["AdapterResult", "LLMAdapter", "ClaudeAdapter", "CodexAdapter"]
