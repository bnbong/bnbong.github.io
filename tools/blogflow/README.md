# blogflow

Local editorial workflow CLI for `bnbong.github.io` — orchestrates `claude` and `codex` CLIs through an approval-gated writing pipeline.

See [blogflow-cli-project-plan.md](./blogflow-cli-project-plan.md) for the product philosophy.

## Install

```bash
pip install -e tools/blogflow
```

Then `blogflow --help` from anywhere in the repo.

## Workflow at a glance

```
ideas → init → brief → answer → draft → review → reflection → finalize → approve → publish
```

Every stage persists artifacts to `.blogflow/sessions/<id>/`. No publish without explicit `blogflow approve`.
