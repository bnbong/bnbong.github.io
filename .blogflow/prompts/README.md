# blogflow prompt overrides

Drop a file named `<stage>.md.j2` here (e.g. `brief.md.j2`, `review.md.j2`) to override the package default for that stage. Templates are Jinja2; the context is whatever the invoking command passes to `blogflow.prompts.render()` — typically a subset of `author`, `session`, `brief`, `answers`, `draft`, `review`, `reflection`, `recent_titles`, and stage-specific keys (see each command module for the exact dict).

If a file is missing here, the packaged template under `blogflow/prompts_tpl/` is used.
