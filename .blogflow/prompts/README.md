# blogflow prompt overrides

Drop a file named `<stage>.md.j2` here (e.g. `brief.md.j2`, `review.md.j2`) to override the package default for that stage. Templates are Jinja2; the session context object is injected as `session`, `brief`, `answers`, `draft`, `review`, `reflection`, and `repo`.

If a file is missing here, the packaged template under `blogflow/prompts_tpl/` is used.
