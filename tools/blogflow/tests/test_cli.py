from __future__ import annotations

import json
import subprocess
from pathlib import Path
from unittest.mock import patch

from click.testing import CliRunner

from blogflow.adapters.base import AdapterResult
from blogflow.cli import cli


def _ok_brief() -> dict:
    return {
        "goal": "understand",
        "learning_brief": "brief",
        "questions": [{"id": "q1", "text": "why?"}],
        "outline": ["Intro"],
        "source_pack": [{"label": "RFC", "url": "https://example"}],
        "scope": "in: x",
        "claim_categories": ["spec"],
    }


def _ok_draft() -> dict:
    return {
        "title_candidates": ["T"],
        "description_candidates": ["d"],
        "body_markdown": "## Intro\n\nhello [SUPPORTED:RFC]\n",
        "claim_summary": [],
        "references": [],
        "known_risks": [],
    }


def _result(
    parsed: dict | None = None, text: str = "", ok: bool = True
) -> AdapterResult:
    return AdapterResult(ok=ok, text=text or json.dumps(parsed or {}), parsed=parsed)


def test_init_and_status(repo_root: Path):
    runner = CliRunner()
    with runner.isolated_filesystem():
        with patch("blogflow.commands._context.find_repo_root", return_value=repo_root):
            res = runner.invoke(
                cli,
                [
                    "init",
                    "--topic",
                    "IPv4",
                    "--post-path",
                    "docs/blog/posts/20260420/new.md",
                ],
            )
            assert res.exit_code == 0, res.output
            assert "Session created" in res.output

            res = runner.invoke(cli, ["status"])
            assert res.exit_code == 0, res.output
            assert "status:   initiated" in res.output
            assert "blogflow brief" in res.output


def test_full_happy_path(repo_root: Path):
    runner = CliRunner()
    with patch("blogflow.commands._context.find_repo_root", return_value=repo_root):
        # init
        assert (
            runner.invoke(
                cli,
                [
                    "init",
                    "--topic",
                    "IPv4",
                    "--post-path",
                    "docs/blog/posts/20260420/new.md",
                ],
            ).exit_code
            == 0
        )

        # brief
        with patch(
            "blogflow.adapters.claude.ClaudeAdapter.run",
            return_value=_result(_ok_brief()),
        ):
            res = runner.invoke(cli, ["brief"])
        assert res.exit_code == 0, res.output

        # answer
        res = runner.invoke(cli, ["answer", "--file", _write_answers(repo_root)])
        assert res.exit_code == 0, res.output

        # draft
        with patch(
            "blogflow.adapters.claude.ClaudeAdapter.run",
            return_value=_result(_ok_draft()),
        ):
            res = runner.invoke(cli, ["draft"])
        assert res.exit_code == 0, res.output

        # review — codex returns APPROVED
        with patch(
            "blogflow.adapters.codex.CodexAdapter.run",
            return_value=AdapterResult(ok=True, text="review body\nGATE: APPROVED"),
        ):
            res = runner.invoke(cli, ["review"])
        assert res.exit_code == 0, res.output
        assert "APPROVED" in res.output

        # reflection --skip
        res = runner.invoke(cli, ["reflection", "--skip"])
        assert res.exit_code == 0, res.output

        # finalize — default now polishes via Claude so review Required-fixes
        # actually reach the final body. The happy path uses --deterministic
        # to keep the mocking surface small.
        res = runner.invoke(cli, ["finalize", "--deterministic"])
        assert res.exit_code == 0, res.output

        # approve
        res = runner.invoke(cli, ["approve"])
        assert res.exit_code == 0, res.output

        # publish
        res = runner.invoke(cli, ["publish"])
        assert res.exit_code == 0, res.output
        post = repo_root / "docs" / "blog" / "posts" / "20260420" / "new.md"
        assert post.exists()
        assert "## Intro" in post.read_text(encoding="utf-8")


def _write_answers(repo_root: Path) -> str:
    p = repo_root / "tmp_answers.yaml"
    p.write_text("answers:\n  q1: because\n", encoding="utf-8")
    return str(p)


def test_review_uses_read_only_sandbox(repo_root: Path):
    """Issue 1: blogflow review must actually call codex with read-only sandbox."""
    runner = CliRunner()
    with patch("blogflow.commands._context.find_repo_root", return_value=repo_root):
        runner.invoke(
            cli,
            [
                "init",
                "--topic",
                "IPv4",
                "--post-path",
                "docs/blog/posts/20260420/new.md",
            ],
        )
        with patch(
            "blogflow.adapters.claude.ClaudeAdapter.run",
            return_value=_result(_ok_brief()),
        ):
            runner.invoke(cli, ["brief"])
        runner.invoke(cli, ["answer", "--file", _write_answers(repo_root)])
        with patch(
            "blogflow.adapters.claude.ClaudeAdapter.run",
            return_value=_result(_ok_draft()),
        ):
            runner.invoke(cli, ["draft"])

        captured: dict = {}

        def _fake_run(self, prompt, *, schema=None, log_dir, stage, extra=None):
            captured["extra"] = extra
            return AdapterResult(ok=True, text="ok\nGATE: APPROVED")

        with patch("blogflow.adapters.codex.CodexAdapter.run", new=_fake_run):
            res = runner.invoke(cli, ["review"])
        assert res.exit_code == 0, res.output
        assert captured["extra"] == {"mode": "review"}


def test_review_manual_gate_recovers_unclear(repo_root: Path):
    """Issue 2: after an UNCLEAR review the author can apply a gate manually
    and the workflow must progress."""
    runner = CliRunner()
    with patch("blogflow.commands._context.find_repo_root", return_value=repo_root):
        runner.invoke(
            cli,
            [
                "init",
                "--topic",
                "IPv4",
                "--post-path",
                "docs/blog/posts/20260420/new.md",
            ],
        )
        with patch(
            "blogflow.adapters.claude.ClaudeAdapter.run",
            return_value=_result(_ok_brief()),
        ):
            runner.invoke(cli, ["brief"])
        runner.invoke(cli, ["answer", "--file", _write_answers(repo_root)])
        with patch(
            "blogflow.adapters.claude.ClaudeAdapter.run",
            return_value=_result(_ok_draft()),
        ):
            runner.invoke(cli, ["draft"])
        # Codex answers without a GATE line → UNCLEAR
        with patch(
            "blogflow.adapters.codex.CodexAdapter.run",
            return_value=AdapterResult(ok=True, text="review body without a verdict"),
        ):
            res = runner.invoke(cli, ["review"])
        assert res.exit_code == 0, res.output
        assert "UNCLEAR" in res.output

        # Status should still be under_review — user hasn't decided yet
        res = runner.invoke(cli, ["status"])
        assert "status:   under_review" in res.output

        # Manual override transitions to awaiting_reflection
        res = runner.invoke(cli, ["review", "--gate", "approved"])
        assert res.exit_code == 0, res.output
        assert "APPROVED" in res.output

        res = runner.invoke(cli, ["status"])
        assert "status:   awaiting_reflection" in res.output


def test_review_revise_loops_back_to_draft(repo_root: Path):
    runner = CliRunner()
    with patch("blogflow.commands._context.find_repo_root", return_value=repo_root):
        runner.invoke(
            cli,
            [
                "init",
                "--topic",
                "IPv4",
                "--post-path",
                "docs/blog/posts/20260420/new.md",
            ],
        )
        with patch(
            "blogflow.adapters.claude.ClaudeAdapter.run",
            return_value=_result(_ok_brief()),
        ):
            runner.invoke(cli, ["brief"])
        runner.invoke(cli, ["answer", "--file", _write_answers(repo_root)])
        with patch(
            "blogflow.adapters.claude.ClaudeAdapter.run",
            return_value=_result(_ok_draft()),
        ):
            runner.invoke(cli, ["draft"])
        with patch(
            "blogflow.adapters.codex.CodexAdapter.run",
            return_value=AdapterResult(ok=True, text="review body\nGATE: REVISE"),
        ):
            res = runner.invoke(cli, ["review"])
        assert "REVISE" in res.output

        res = runner.invoke(cli, ["status"])
        assert "status:   draft_ready" in res.output


def test_publish_post_path_override_sets_target(repo_root: Path):
    """`blogflow init` run without --post-path leaves target_post_path=None;
    the publish command's --post-path flag must be able to set it retroactively
    so the author doesn't have to restart the whole workflow."""
    runner = CliRunner()
    with patch("blogflow.commands._context.find_repo_root", return_value=repo_root):
        # init WITHOUT --post-path (the scenario that previously blocked publish)
        runner.invoke(cli, ["init", "--topic", "IPv4"])
        with patch(
            "blogflow.adapters.claude.ClaudeAdapter.run",
            return_value=_result(_ok_brief()),
        ):
            runner.invoke(cli, ["brief"])
        runner.invoke(cli, ["answer", "--file", _write_answers(repo_root)])
        with patch(
            "blogflow.adapters.claude.ClaudeAdapter.run",
            return_value=_result(_ok_draft()),
        ):
            runner.invoke(cli, ["draft"])
        with patch(
            "blogflow.adapters.codex.CodexAdapter.run",
            return_value=AdapterResult(ok=True, text="ok\nGATE: APPROVED"),
        ):
            runner.invoke(cli, ["review"])
        runner.invoke(cli, ["reflection", "--skip"])
        runner.invoke(cli, ["finalize", "--deterministic"])
        runner.invoke(cli, ["approve"])

        # Without the override flag, publish errors out with the usual guard.
        res = runner.invoke(cli, ["publish"])
        assert res.exit_code != 0
        assert "target_post_path" in str(res.exception)

        # With --post-path the target gets set and publish succeeds.
        target_rel = "docs/blog/posts/20260420-recovery/post.md"
        res = runner.invoke(cli, ["publish", "--post-path", target_rel])
        assert res.exit_code == 0, res.output
        assert (repo_root / target_rel).exists()


def test_review_loop_cap_stops_auto_transition(repo_root: Path):
    """After MAX_AUTO_REVISE auto cycles, a REVISE must NOT transition back to
    draft — it should park the session and tell the author to pick a manual
    gate. This is what stops the reviewer/draft loop from burning tokens on
    non-blocking nits."""
    runner = CliRunner()
    with patch("blogflow.commands._context.find_repo_root", return_value=repo_root):
        runner.invoke(
            cli,
            ["init", "--topic", "IPv4", "--post-path", "docs/blog/posts/cap/cap.md"],
        )
        with patch(
            "blogflow.adapters.claude.ClaudeAdapter.run",
            return_value=_result(_ok_brief()),
        ):
            runner.invoke(cli, ["brief"])
        runner.invoke(cli, ["answer", "--file", _write_answers(repo_root)])

        # First draft → review (REVISE). Auto-loops once.
        with patch(
            "blogflow.adapters.claude.ClaudeAdapter.run",
            return_value=_result(_ok_draft()),
        ):
            runner.invoke(cli, ["draft"])
        with patch(
            "blogflow.adapters.codex.CodexAdapter.run",
            return_value=AdapterResult(ok=True, text="body\nGATE: REVISE"),
        ):
            runner.invoke(cli, ["review"])

        # Second draft → review (REVISE again). Cap fires here.
        with patch(
            "blogflow.adapters.claude.ClaudeAdapter.run",
            return_value=_result(_ok_draft()),
        ):
            runner.invoke(cli, ["draft"])
        with patch(
            "blogflow.adapters.codex.CodexAdapter.run",
            return_value=AdapterResult(ok=True, text="body\nGATE: REVISE"),
        ):
            res = runner.invoke(cli, ["review"])

        # Output must nudge toward manual gate; status must stay at under_review
        # (i.e. NOT loop back to draft_ready).
        assert "Auto-loop stopped" in res.output
        assert "--gate" in res.output
        status_res = runner.invoke(cli, ["status"])
        assert "status:   under_review" in status_res.output


def test_init_auto_increments_on_same_minute_topic(repo_root: Path):
    """Issue 5: repeated init within the same minute for the same topic must
    produce distinct session dirs rather than silently reusing one."""
    runner = CliRunner()
    with patch("blogflow.commands._context.find_repo_root", return_value=repo_root):
        r1 = runner.invoke(
            cli,
            ["init", "--topic", "IPv4", "--post-path", "docs/blog/posts/a/a.md"],
        )
        assert r1.exit_code == 0, r1.output
        r2 = runner.invoke(
            cli,
            ["init", "--topic", "IPv4", "--post-path", "docs/blog/posts/b/b.md"],
        )
        assert r2.exit_code == 0, r2.output

        sessions_dir = repo_root / ".blogflow" / "sessions"
        sessions = sorted(p.name for p in sessions_dir.iterdir() if p.is_dir())
        assert len(sessions) == 2, sessions
        assert sessions[0] != sessions[1]


def test_editor_flow_splits_env_with_flags(
    repo_root: Path, tmp_path: Path, monkeypatch
):
    """Issue 4: `EDITOR='code --wait'` must not be treated as a single executable name."""
    from blogflow.commands import reflection as reflection_mod

    # Prime a session so the reflection command can run at awaiting_reflection.
    runner = CliRunner()
    with patch("blogflow.commands._context.find_repo_root", return_value=repo_root):
        runner.invoke(
            cli,
            ["init", "--topic", "IPv4", "--post-path", "docs/blog/posts/a/a.md"],
        )
        with patch(
            "blogflow.adapters.claude.ClaudeAdapter.run",
            return_value=_result(_ok_brief()),
        ):
            runner.invoke(cli, ["brief"])
        runner.invoke(cli, ["answer", "--file", _write_answers(repo_root)])
        with patch(
            "blogflow.adapters.claude.ClaudeAdapter.run",
            return_value=_result(_ok_draft()),
        ):
            runner.invoke(cli, ["draft"])
        with patch(
            "blogflow.adapters.codex.CodexAdapter.run",
            return_value=AdapterResult(ok=True, text="ok\nGATE: APPROVED"),
        ):
            runner.invoke(cli, ["review"])

        captured: dict = {}

        def fake_run(argv, check=False):
            captured["argv"] = argv
            # Simulate the editor writing reflection content into the tmpfile.
            file_path = Path(argv[-1])
            file_path.write_text(
                "# primer comment\n\n내가 배운 것: 네트워크.\n", encoding="utf-8"
            )
            return subprocess.CompletedProcess(args=argv, returncode=0)

        monkeypatch.setenv("EDITOR", "code --wait")
        monkeypatch.setattr(reflection_mod.subprocess, "run", fake_run)

        res = runner.invoke(cli, ["reflection"])
        assert res.exit_code == 0, res.output
        assert captured["argv"][:2] == ["code", "--wait"]
        assert captured["argv"][-1].endswith(".md")

        reflection_path = (
            repo_root
            / ".blogflow"
            / "sessions"
            / _only_session(repo_root)
            / "user"
            / "reflection.md"
        )
        assert "내가 배운 것" in reflection_path.read_text(encoding="utf-8")


def _only_session(repo_root: Path) -> str:
    d = repo_root / ".blogflow" / "sessions"
    dirs = [p for p in d.iterdir() if p.is_dir()]
    assert len(dirs) == 1, dirs
    return dirs[0].name


def test_status_default_picks_session_saved_last(repo_root: Path):
    """Finding 1: back-to-back `init` of two different topics used to leave
    default `blogflow status` pointing at the FIRST session because both
    sessions' updated_at tied at second precision. The new session must win."""
    runner = CliRunner()
    with patch("blogflow.commands._context.find_repo_root", return_value=repo_root):
        res_a = runner.invoke(
            cli,
            ["init", "--topic", "IPv4", "--post-path", "docs/blog/posts/a/a.md"],
        )
        assert res_a.exit_code == 0, res_a.output
        res_b = runner.invoke(
            cli,
            ["init", "--topic", "IPv6", "--post-path", "docs/blog/posts/b/b.md"],
        )
        assert res_b.exit_code == 0, res_b.output

        # No --session supplied → default latest-session resolution.
        res = runner.invoke(cli, ["status"])
        assert res.exit_code == 0, res.output
        assert "IPv6" in res.output, res.output
        assert "ipv6" in res.output, res.output


def test_finalize_defaults_to_regenerate_so_review_is_applied(repo_root: Path):
    """Finding 2: the default `blogflow finalize` must actually consume the
    review — not silently concatenate draft + reflection. Previously the
    deterministic merge was the default and review Required-fixes were dropped.
    """
    runner = CliRunner()
    with patch("blogflow.commands._context.find_repo_root", return_value=repo_root):
        runner.invoke(
            cli,
            ["init", "--topic", "IPv4", "--post-path", "docs/blog/posts/f/f.md"],
        )
        with patch(
            "blogflow.adapters.claude.ClaudeAdapter.run",
            return_value=_result(_ok_brief()),
        ):
            runner.invoke(cli, ["brief"])
        runner.invoke(cli, ["answer", "--file", _write_answers(repo_root)])
        with patch(
            "blogflow.adapters.claude.ClaudeAdapter.run",
            return_value=_result(_ok_draft()),
        ):
            runner.invoke(cli, ["draft"])
        with patch(
            "blogflow.adapters.codex.CodexAdapter.run",
            return_value=AdapterResult(
                ok=True,
                text=(
                    "### Required fixes (blocking)\n"
                    "1. Fix the bogus sentence.\n\n"
                    "### Suggestions (non-blocking)\n"
                    "- Add more examples.\n\n"
                    "GATE: APPROVED"
                ),
            ),
        ):
            runner.invoke(cli, ["review"])
        runner.invoke(cli, ["reflection", "--skip"])

        # Capture the finalize prompt so we can check that review content
        # actually reached Claude (i.e. finalize did not fall back to the
        # deterministic merge that ignores review.md).
        finalize_calls: list = []

        def _fake_finalize(self, prompt, *, schema=None, log_dir, stage, extra=None):
            finalize_calls.append({"prompt": prompt, "stage": stage})
            return AdapterResult(
                ok=True,
                text="## Intro\n\nRewritten with required fix applied.\n",
            )

        with patch("blogflow.adapters.claude.ClaudeAdapter.run", new=_fake_finalize):
            res = runner.invoke(cli, ["finalize"])
        assert res.exit_code == 0, res.output

        assert len(finalize_calls) == 1, finalize_calls
        rendered_prompt = finalize_calls[0]["prompt"]
        assert "Fix the bogus sentence." in rendered_prompt
        assert "Required fixes" in rendered_prompt

        final_md = (
            repo_root
            / ".blogflow"
            / "sessions"
            / _only_session(repo_root)
            / "outputs"
            / "final.md"
        )
        assert "Rewritten with required fix applied." in final_md.read_text(
            encoding="utf-8"
        )


def test_finalize_deterministic_flag_skips_claude(repo_root: Path):
    """Authors can still opt out of the Claude polish — but it must be an
    explicit choice."""
    runner = CliRunner()
    with patch("blogflow.commands._context.find_repo_root", return_value=repo_root):
        runner.invoke(
            cli,
            ["init", "--topic", "IPv4", "--post-path", "docs/blog/posts/d/d.md"],
        )
        with patch(
            "blogflow.adapters.claude.ClaudeAdapter.run",
            return_value=_result(_ok_brief()),
        ):
            runner.invoke(cli, ["brief"])
        runner.invoke(cli, ["answer", "--file", _write_answers(repo_root)])
        with patch(
            "blogflow.adapters.claude.ClaudeAdapter.run",
            return_value=_result(_ok_draft()),
        ):
            runner.invoke(cli, ["draft"])
        with patch(
            "blogflow.adapters.codex.CodexAdapter.run",
            return_value=AdapterResult(ok=True, text="ok\nGATE: APPROVED"),
        ):
            runner.invoke(cli, ["review"])
        runner.invoke(cli, ["reflection", "--skip"])

        # --deterministic must NOT call Claude.
        called = {"n": 0}

        def _should_not_be_called(*a, **kw):
            called["n"] += 1
            raise AssertionError("claude adapter must not run when --deterministic")

        with patch("blogflow.adapters.claude.ClaudeAdapter.run", new=_should_not_be_called):
            res = runner.invoke(cli, ["finalize", "--deterministic"])
        assert res.exit_code == 0, res.output
        assert called["n"] == 0


def test_published_post_has_no_provenance_markers(repo_root: Path):
    """Finding 3: the published post must not expose `[SUPPORTED:…]` / `[ASSUMED]`
    audit markers. This covers the `--deterministic` path because that is the
    code path that currently keeps the raw draft body (no LLM polish), which
    is where the markers would otherwise survive into the public post."""
    runner = CliRunner()
    with patch("blogflow.commands._context.find_repo_root", return_value=repo_root):
        runner.invoke(
            cli,
            ["init", "--topic", "IPv4", "--post-path", "docs/blog/posts/p/p.md"],
        )
        with patch(
            "blogflow.adapters.claude.ClaudeAdapter.run",
            return_value=_result(_ok_brief()),
        ):
            runner.invoke(cli, ["brief"])
        runner.invoke(cli, ["answer", "--file", _write_answers(repo_root)])

        dirty_draft = dict(_ok_draft())
        dirty_draft["body_markdown"] = (
            "## Intro\n\n"
            "IPv4 헤더는 20 바이트이다 [SUPPORTED:RFC 791].\n"
            "이 주장은 검증되지 않았다 [ASSUMED].\n"
        )
        with patch(
            "blogflow.adapters.claude.ClaudeAdapter.run",
            return_value=_result(dirty_draft),
        ):
            runner.invoke(cli, ["draft"])
        with patch(
            "blogflow.adapters.codex.CodexAdapter.run",
            return_value=AdapterResult(ok=True, text="ok\nGATE: APPROVED"),
        ):
            runner.invoke(cli, ["review"])
        runner.invoke(cli, ["reflection", "--skip"])
        # Use --deterministic so the test does not need to mock Claude again;
        # the provenance scrub must run on both paths, so this is a strict
        # regression check on the strip step itself.
        res = runner.invoke(cli, ["finalize", "--deterministic"])
        assert res.exit_code == 0, res.output

        final_md = (
            repo_root
            / ".blogflow"
            / "sessions"
            / _only_session(repo_root)
            / "outputs"
            / "final.md"
        ).read_text(encoding="utf-8")
        assert "[SUPPORTED:" not in final_md, final_md
        assert "[ASSUMED]" not in final_md, final_md

        runner.invoke(cli, ["approve"])
        res = runner.invoke(cli, ["publish"])
        assert res.exit_code == 0, res.output
        post = (repo_root / "docs" / "blog" / "posts" / "p" / "p.md").read_text(
            encoding="utf-8"
        )
        assert "[SUPPORTED:" not in post, post
        assert "[ASSUMED]" not in post, post
