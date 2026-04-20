"""
MkDocs Recent Posts Hook

Replaces the <!-- RECENT_POSTS:START --> / <!-- RECENT_POSTS:END --> block in
index.md with the latest N blog posts rendered as Material grid cards.

Reads frontmatter (title, date.created, categories, tags) from every
docs/blog/posts/**/*.md and sorts by date descending. Future-dated posts
(treated as drafts by the blog plugin) are filtered out.

Author: bnbong
"""

import re
from datetime import date, datetime
from pathlib import Path

import yaml

MARKER_START = "<!-- RECENT_POSTS:START -->"
MARKER_END = "<!-- RECENT_POSTS:END -->"
POST_COUNT = 3
MAX_TAGS_IN_META = 3


def _parse_frontmatter(text):
    if not text.startswith("---"):
        return {}, text
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}, text
    try:
        meta = yaml.safe_load(parts[1]) or {}
    except yaml.YAMLError:
        meta = {}
    return meta, parts[2]


def _coerce_date(value):
    if isinstance(value, datetime):
        return value.date()
    if isinstance(value, date):
        return value
    if isinstance(value, str):
        try:
            return date.fromisoformat(value)
        except ValueError:
            return None
    return None


def _get_created(meta):
    d = meta.get("date")
    if isinstance(d, dict):
        d = d.get("created") or d.get("updated")
    return _coerce_date(d)


def _collect_posts(docs_dir):
    today = date.today()
    posts = []
    posts_dir = docs_dir / "blog" / "posts"
    if not posts_dir.exists():
        return posts
    for md_path in posts_dir.rglob("*.md"):
        try:
            text = md_path.read_text(encoding="utf-8")
        except OSError:
            continue
        meta, _ = _parse_frontmatter(text)
        if not meta or meta.get("draft") is True:
            continue
        created = _get_created(meta)
        if created is None or created > today:
            continue
        rel = md_path.relative_to(docs_dir).as_posix()
        posts.append(
            {
                "title": str(meta.get("title", md_path.stem)),
                "date": created,
                "categories": meta.get("categories") or [],
                "tags": meta.get("tags") or [],
                "path": rel,
            }
        )
    posts.sort(key=lambda p: p["date"], reverse=True)
    return posts


def _card_markdown(post):
    cats = " / ".join(str(c) for c in post["categories"])
    tags = " / ".join(str(t) for t in post["tags"][:MAX_TAGS_IN_META])
    meta_parts = [post["date"].isoformat()]
    if cats:
        meta_parts.append(cats)
    if tags:
        meta_parts.append(tags)
    meta_line = " · ".join(meta_parts)
    return (
        f"-   :material-calendar-text:{{ .lg .middle }} **{post['title']}**\n\n"
        f"    ---\n\n"
        f"    {meta_line}\n\n"
        f"    [포스트 읽기 →]({post['path']})\n"
    )


def _render_block(posts):
    cards = "\n".join(_card_markdown(p) for p in posts[:POST_COUNT])
    return (
        f"{MARKER_START}\n\n"
        f'<div class="grid cards" markdown>\n\n'
        f"{cards}\n"
        f"</div>\n\n"
        f"{MARKER_END}"
    )


def on_page_markdown(markdown, *, page, config, files, **_kwargs):
    if page.file.src_uri != "index.md":
        return markdown
    if MARKER_START not in markdown or MARKER_END not in markdown:
        return markdown
    posts = _collect_posts(Path(config["docs_dir"]))
    if not posts:
        return markdown
    pattern = re.compile(
        re.escape(MARKER_START) + r".*?" + re.escape(MARKER_END),
        re.DOTALL,
    )
    return pattern.sub(_render_block(posts), markdown)
