"""Typed errors used across blogflow commands."""

from __future__ import annotations


class BlogflowError(Exception):
    """Base class."""


class StateError(BlogflowError):
    """Illegal workflow transition."""

    def __init__(self, message: str, expected_command: str | None = None):
        super().__init__(message)
        self.expected_command = expected_command


class AdapterError(BlogflowError):
    """LLM adapter invocation failure."""


class PublishError(BlogflowError):
    """Safety guard tripped during publish."""


class SessionNotFoundError(BlogflowError):
    """No session resolvable from CLI arguments."""


class ConfigError(BlogflowError):
    """Config file missing or malformed."""
