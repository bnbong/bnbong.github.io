"""Click entrypoint for the `blogflow` CLI."""

from __future__ import annotations

import sys

import click

from . import __version__
from .commands.answer import answer_cmd
from .commands.approve import approve_cmd
from .commands.brief import brief_cmd
from .commands.draft import draft_cmd
from .commands.finalize import finalize_cmd
from .commands.ideas import ideas_cmd
from .commands.init import init_cmd
from .commands.publish import publish_cmd
from .commands.reflection import reflection_cmd
from .commands.review import review_cmd
from .commands.status import status_cmd
from .errors import BlogflowError


@click.group(context_settings={"help_option_names": ["-h", "--help"]})
@click.version_option(__version__, "-V", "--version")
def cli() -> None:
    """Local-first editorial workflow for bnbong.github.io."""


for _cmd in (
    ideas_cmd,
    init_cmd,
    status_cmd,
    brief_cmd,
    answer_cmd,
    draft_cmd,
    review_cmd,
    reflection_cmd,
    finalize_cmd,
    approve_cmd,
    publish_cmd,
):
    cli.add_command(_cmd)


def main() -> None:
    try:
        cli(standalone_mode=True)
    except BlogflowError as exc:
        click.echo(f"error: {exc}", err=True)
        hint = getattr(exc, "expected_command", None)
        if hint:
            click.echo(f"hint: next expected — {hint}", err=True)
        sys.exit(1)


if __name__ == "__main__":
    main()
