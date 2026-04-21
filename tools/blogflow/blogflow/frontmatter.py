"""Safe YAML frontmatter read / update for MkDocs post files."""

from __future__ import annotations

import os
import tempfile
from pathlib import Path

import yaml

from .errors import PublishError
from .models import Frontmatter

FENCE = "---"


class _NoAliasDumper(yaml.SafeDumper):
    """PyYAML emits `&id001` / `*id001` anchors when the same Python object
    appears twice in a mapping (e.g. `date.created` and `date.updated` both
    bound to the same `datetime.date`). mkdocs-material's blog plugin doesn't
    follow those aliases and the CI build fails on the first post that hits
    this path. Disabling aliases keeps the serialized frontmatter trivially
    readable for both humans and the plugin.
    """

    def ignore_aliases(self, data):  # noqa: ARG002
        return True


def parse(text: str) -> Frontmatter:
    if not text.startswith(FENCE):
        return Frontmatter(raw={}, body=text)
    parts = text.split(FENCE, 2)
    if len(parts) < 3:
        raise PublishError("Frontmatter fence opened but not closed.")
    try:
        meta = yaml.safe_load(parts[1]) or {}
    except yaml.YAMLError as exc:
        raise PublishError(f"Invalid YAML frontmatter: {exc}") from exc
    if not isinstance(meta, dict):
        raise PublishError("Frontmatter must be a YAML mapping.")
    body = parts[2].lstrip("\n")
    return Frontmatter(raw=meta, body=body)


def read(path: Path) -> Frontmatter:
    return parse(path.read_text(encoding="utf-8"))


def dump(fm: Frontmatter) -> str:
    yaml_text = yaml.dump(
        fm.raw,
        Dumper=_NoAliasDumper,
        sort_keys=False,
        allow_unicode=True,
        default_flow_style=False,
    ).rstrip("\n")
    body = fm.body
    if body and not body.endswith("\n"):
        body += "\n"
    return f"{FENCE}\n{yaml_text}\n{FENCE}\n\n{body}"


def write_atomic(path: Path, fm: Frontmatter) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    content = dump(fm)
    fd, tmp_path = tempfile.mkstemp(prefix=path.name + ".", dir=str(path.parent))
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            f.write(content)
        os.replace(tmp_path, path)
    except Exception:
        try:
            os.unlink(tmp_path)
        except FileNotFoundError:
            pass
        raise
