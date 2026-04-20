# blogflow CLI Project Plan

## 1. Overview

`blogflow` is a local-first editorial workflow CLI for writing technical blog posts with strong human supervision.

The purpose of the tool is **not** to let AI fully author and publish posts autonomously. Instead, it should help the author:

- choose or refine topics,
- gather and approve sources,
- review concept summaries before drafting,
- lock the writing scope and post structure,
- draft posts with source-aware constraints,
- run a second-model review before publishing,
- optionally add a personal reflection section,
- require explicit human approval before publish.

This plan is based on the full discussion history for the project, including:

- the desire to publish steadily at a pace of roughly 2-3 posts per week,
- the requirement that the author remain deeply involved in topic selection, concept validation, structure, and final approval,
- the need to reduce hallucination risk as much as possible for technical writing,
- the preference for attaching external references when appropriate,
- the requirement that the final "reflection" section remain optional,
- the available local environment: macOS, `claude` CLI installed, `codex` CLI installed.

## 2. Problem Statement

The current blog workflow is good for manual writing, but it does not provide a structured editorial system for:

- topic backlog management,
- source approval,
- human-in-the-loop concept review,
- claim tracking,
- multi-model review,
- approval-gated publishing,
- repeatable local execution.

Without structure, consistent publication becomes difficult. Without source controls, technical post quality becomes vulnerable to LLM hallucination and overconfident simplification.

## 3. Goals

### Primary goals

- Build a repeatable local CLI workflow for technical blog writing.
- Keep the author in control of concept, scope, flow, and publishing.
- Use AI for summarization, drafting, and review support.
- Reduce hallucination risk using explicit workflow gates.
- Make the workflow practical enough to support 2-3 posts per week.

### Secondary goals

- Reuse the workflow across different post types:
  - concept explainers,
  - project retrospectives,
  - troubleshooting notes,
  - OSS contribution records.
- Preserve intermediate artifacts for later inspection and revision.
- Support topic suggestion as well as author-driven topic selection.

## 4. Non-Goals

- No fully autonomous publishing.
- No background daemon, server, or hosted workflow engine.
- No web dashboard or GUI in the MVP.
- No mandatory Git push automation in the MVP.
- No multi-user collaboration features.
- No attempt to mathematically guarantee zero hallucination. Instead, the workflow must make unsupported claims visible and block them from publish readiness.

## 5. Constraints

### Editorial constraints

- Technical posts require source-aware writing.
- The author wants to review summarized concepts before drafting.
- The author wants AI to ask focused questions only when human judgment is genuinely needed.
- The "reflection" or "what I learned" section must be optional.
- Final publishing must require explicit human approval.

### Environment constraints

- The tool will run only on the author's local MacBook (macOS).
- Local tools already available:
  - `claude`
  - `codex`
- The repository is a MkDocs-based blog with posts under `docs/blog/posts/...`.
- `n8n` is intentionally not part of the solution.

## 6. Core Product Philosophy

`blogflow` is a **local editorial orchestrator**, not an autonomous author.

It should behave like a careful assistant that:

- organizes workflow state,
- invokes Claude and Codex when needed,
- stores prompts, outputs, and user decisions,
- enforces gates before advancing,
- makes the author's involvement lightweight but meaningful.

## 7. Human and AI Roles

### Author

The author is responsible for:

- selecting or approving the topic,
- approving the source pack,
- answering scope and audience questions,
- reviewing the outline direction,
- approving the final draft,
- optionally writing personal reflection input,
- approving publish.

### Claude

Claude acts as the **editorial director and primary drafter**:

- topic recommendation,
- brief generation,
- source pack suggestion,
- question generation,
- outline generation,
- first-pass drafting,
- optional reflection prompting,
- revision support after review.

### Codex

Codex acts as the **technical review and publish gate checker**:

- identify unsupported or weakly supported claims,
- detect over-simplifications,
- flag terminology risk,
- check structure and repository-fit,
- inspect factual and wording risks before publish.

## 8. Hallucination Control Strategy

The workflow must reduce hallucination risk by process, not by trust.

### Required mechanisms

- **Source gate**: approved source set before drafting.
- **Brief gate**: author reviews the conceptual summary before draft generation.
- **Question gate**: AI asks focused questions to resolve scope ambiguity.
- **Claim awareness**: draft generation should surface key factual claims and uncertain areas.
- **Second-model review**: Codex reviews Claude output before finalization.
- **Approval gate**: no publish without explicit human approval.

### Operational principle

The workflow should treat unsupported claims as workflow defects, not stylistic noise.

## 9. Supported Post Entry Modes

`blogflow` must support two ways to begin:

### Author-selected topic

The author provides the topic directly.

Examples:

- IPv4 concept explainer
- FastAPI FastKit design lessons
- K-Buddy infra retrospective

### AI-suggested topic

Claude proposes topics based on:

- recent repo/project activity,
- open project material,
- recurring study themes,
- gaps in existing blog coverage,
- author experience likely to produce high-value posts.

Each topic suggestion should ideally include:

- title idea,
- why now,
- intended audience,
- expected difficulty,
- source requirements,
- hallucination risk,
- whether the topic is suitable for a single post or a series.

## 10. End-to-End Workflow

### Workflow summary

1. Topic selection
2. Session initialization
3. Source pack generation
4. Brief generation
5. User answers / scope decisions
6. Outline generation
7. Draft generation
8. Codex review
9. Draft revision
10. Optional reflection
11. Finalization
12. Approval
13. Publish

### Reflection rule

Reflection is optional:

- if the author answers the reflection prompt, include the section,
- if the author skips or leaves it empty, do not create the section.

## 11. Status Machine

Each post session should move through an explicit status machine.

Recommended states:

- `initiated`
- `brief_ready`
- `awaiting_answers`
- `draft_ready`
- `under_review`
- `awaiting_reflection`
- `final_ready`
- `approved`
- `published`

Illegal transitions should be blocked.

Examples:

- no review before a draft exists,
- no finalize before review,
- no publish before approval.

## 12. Recommended Session Artifact Layout

Each session should be stored in a dedicated folder under `.blogflow/`.

```text
.blogflow/
  config.yaml
  sessions/
    <session-id>/
      session.yaml
      prompts/
        brief.txt
        draft.txt
        review.txt
        finalize.txt
        reflection.txt
      outputs/
        brief.json
        draft.md
        review.md
        final.md
      user/
        answers.yaml
        reflection.md
      schemas/
        brief.schema.json
        draft.schema.json
        review.schema.json
```

This layout must support:

- reproducibility,
- restartability,
- auditability,
- debugging prompt quality later.

## 13. CLI Command Set (MVP)

The MVP command set should be:

- `blogflow ideas`
- `blogflow init`
- `blogflow status`
- `blogflow brief`
- `blogflow answer`
- `blogflow draft`
- `blogflow review`
- `blogflow reflection`
- `blogflow finalize`
- `blogflow approve`
- `blogflow publish`

### Command intent

#### `blogflow ideas`

- ask Claude to propose topic candidates,
- optionally scoped by category or difficulty,
- store or print candidates.

#### `blogflow init`

- start a session for a specific post or topic,
- create session folder and metadata,
- bind target post path if already known.

#### `blogflow status`

- show current status,
- show existing artifacts,
- suggest next valid command.

#### `blogflow brief`

- invoke Claude with the briefing prompt,
- generate:
  - one-line goal,
  - learning brief,
  - source pack proposal,
  - scope,
  - questions,
  - outline v1,
  - claim categories,
- persist outputs.

#### `blogflow answer`

- capture author decisions from the brief stage,
- update session metadata and answer artifacts.

#### `blogflow draft`

- invoke Claude to generate:
  - title candidates,
  - description candidates,
  - first draft,
  - claim summary,
  - references draft,
  - known risks for Codex review.

#### `blogflow review`

- invoke Codex to review the draft,
- produce findings and gate decision,
- flag unsupported claims or risky wording.

#### `blogflow reflection`

- optionally ask the author reflection questions,
- persist response if provided,
- allow clean skip.

#### `blogflow finalize`

- combine:
  - draft,
  - review feedback,
  - optional reflection,
- generate final candidate output,
- keep publish blocked until approval.

#### `blogflow approve`

- record explicit human approval in session state.

#### `blogflow publish`

- write final content into target post file,
- ensure `draft: false`,
- update `date.updated`,
- print suggested Git commands,
- do not auto-push in MVP.

## 14. Integration with Claude and Codex

### Claude invocation

Prefer structured non-interactive execution.

Recommended direction:

- `claude -p`
- `--output-format json`
- `--json-schema ...`

Fallback:

- raw text output saved to artifact files when structured output is unavailable.

### Codex invocation

Prefer non-interactive execution and review mode.

Possible direction:

- `codex exec --output-schema ...`
- `codex review ...` when the interaction maps naturally to review semantics

### Adapter rule

LLM invocation must be isolated behind adapter modules so that:

- prompt logic stays separate from transport,
- retries and fallback behavior can be added later,
- tests can mock process execution cleanly.

## 15. Prompt Strategy

Prompt design should be modular and stage-specific.

Required prompt categories:

- ideas prompt
- brief prompt
- draft prompt
- review prompt
- finalize prompt
- reflection prompt

Prompt builders should accept session context instead of hardcoding a single topic.

The IPv4 post used during planning should serve as one concrete example, not a special case baked into business logic.

## 16. Publish Safety Rules

The tool must be conservative at publish time.

### Required checks before publish

- final artifact exists,
- session status is `approved`,
- target post path is defined,
- frontmatter remains valid,
- `draft: false` will be applied,
- `date.updated` will be refreshed,
- final output is present on disk.

### Explicitly out of scope for MVP

- automatic Git commit,
- automatic Git push,
- automatic GitHub deployment.

The tool may print recommended next commands such as:

```bash
git add <post-path> .blogflow/sessions/<session-id>
git commit -m "Add IPv4 blog post draft"
git push origin main
```

## 17. UX Expectations

The CLI should be practical and calm, not overly magical.

Each command should:

- explain what it did,
- list generated files,
- show current status,
- suggest the next likely command.

Errors should be actionable.

Examples:

- "Cannot run review before draft generation."
- "Cannot publish before approval."
- "Brief exists but answers are missing. Run `blogflow answer` next."

## 18. Recommended Implementation Shape

### Language

- Python

### Recommended libraries

- `click`
- `PyYAML`
- standard library `subprocess`
- optional `Jinja2` for prompt templating

### Recommended module layout

```text
tools/blogflow/
  cli.py
  state.py
  models.py
  prompts.py
  frontmatter.py
  publish.py
  schemas.py
  adapters/
    claude.py
    codex.py
```

### Design rules

- small modules,
- testable logic,
- no monolithic command handler,
- clear separation between:
  - workflow state,
  - prompt generation,
  - LLM process execution,
  - post file mutation.

## 19. Testing Strategy

The MVP should include tests for:

- session creation,
- state transitions,
- invalid state transition blocking,
- frontmatter read/write,
- publish mutation safety,
- prompt artifact creation,
- adapter mocking for Claude and Codex calls.

Tests should not depend on real LLM execution.

## 20. Phased Delivery Plan

### Phase 1: MVP

- implement all listed commands,
- session state management,
- prompt/output artifact storage,
- Claude draft flow,
- Codex review flow,
- approval-gated publish.

### Phase 2: Quality improvements

- richer source pack support,
- stronger claim artifact structure,
- prompt externalization,
- improved schema validation,
- reusable prompt presets by post type.

### Phase 3: Convenience features

- git helper commands,
- topic backlog view,
- stronger repo introspection,
- scheduling helpers,
- template presets for:
  - explainer,
  - project retrospective,
  - troubleshooting note,
  - OSS contribution post.

## 21. Risks and Mitigations

### Risk: LLM output inconsistency

Mitigation:

- structured output where possible,
- save raw prompts and outputs,
- allow rerun of any stage.

### Risk: hidden hallucinations in technically familiar topics

Mitigation:

- source pack requirement,
- Codex review gate,
- manual approval.

### Risk: too much friction to sustain weekly writing

Mitigation:

- keep commands short,
- preserve intermediate state,
- allow lite usage for simple posts,
- reserve stricter review for high-risk posts.

### Risk: publish becomes too automated

Mitigation:

- no publish without explicit approval,
- no automatic push in MVP.

## 22. Acceptance Criteria

The project can be considered successful when:

- the author can run the workflow entirely on local macOS,
- a new session can be created for a post like `IPv4`,
- Claude can generate a brief and first draft through `blogflow`,
- Codex can review the draft through `blogflow`,
- the author can skip reflection cleanly,
- the author must explicitly approve before publish,
- publish writes the final post content safely without automatically pushing Git changes,
- all intermediate artifacts are saved and inspectable.

## 23. Example Success Case: IPv4 Post

Example target:

- file: `docs/blog/posts/20250117-computer-network-3/20250117.md`
- topic: `IPv4`
- workflow:
  - init session,
  - generate brief and source pack,
  - answer scope questions,
  - generate draft,
  - run Codex review,
  - revise/finalize,
  - optionally skip reflection,
  - approve,
  - publish.

If that flow works end-to-end with saved artifacts and no unsafe automation, the MVP is functionally validated.

## 24. Final Recommendation

`blogflow` should be implemented as a **local Python CLI application**.

That is the best fit because:

- the workflow is stateful,
- the author is on macOS only,
- both `claude` and `codex` CLIs already exist locally,
- the problem is orchestration and safety, not hosting,
- the author wants strong human supervision and artifact visibility.

This means the next practical step is to hand this plan and the implementation prompt to Claude Opus 4.7 and ask it to build the MVP inside the repository.
