from textwrap import dedent
import urllib.parse
import re

fb_sharer = "https://www.facebook.com/sharer/sharer.php"
thread_intent = "https://threads.net/intent/post"
include = re.compile(r"blog/[1-9].*")


def on_page_markdown(markdown, **kwargs):
    page = kwargs['page']
    config = kwargs['config']
    if not include.match(page.url):
        return markdown

    page_url = config.site_url+page.url
    page_title = urllib.parse.quote(page.title+'\n')

    return markdown + dedent(f"""
    [Share on :simple-facebook:]({fb_sharer}?u={page_url}){{ .md-button }}
    [Share on :simple-threads:]({thread_intent}?text={page_title}&linkurl={page_url}){{ .md-button }}
    """)
