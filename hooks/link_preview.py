"""
MkDocs Link Preview Hook

Converts ```preview code blocks with URLs into social card-style HTML previews
using Open Graph metadata.

Usage in markdown example:

```preview
https://www.acmicpc.net/problem/1436
```

Author: bnbong
"""

import re
import hashlib
import json
from pathlib import Path
from typing import Optional, Dict
from urllib.parse import urlparse

try:
    import requests
    from bs4 import BeautifulSoup
    HAS_DEPENDENCIES = True
except ImportError:
    HAS_DEPENDENCIES = False

# Cache directory for OG metadata
CACHE_DIR = Path(__file__).parent.parent / ".cache" / "link_preview"

# Regex pattern to match ```preview code blocks
PREVIEW_PATTERN = re.compile(
    r'```preview\s*\n(https?://[^\s]+)\s*\n```',
    re.MULTILINE
)


def get_cache_path(url: str) -> Path:
    """Generate cache file path for a URL."""
    url_hash = hashlib.md5(url.encode()).hexdigest()
    return CACHE_DIR / f"{url_hash}.json"


def load_from_cache(url: str) -> Optional[Dict]:
    """Load cached OG metadata if available."""
    cache_path = get_cache_path(url)
    if cache_path.exists():
        try:
            with open(cache_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            pass
    return None


def save_to_cache(url: str, metadata: Dict) -> None:
    """Save OG metadata to cache."""
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    cache_path = get_cache_path(url)
    try:
        with open(cache_path, 'w', encoding='utf-8') as f:
            json.dump(metadata, f, ensure_ascii=False, indent=2)
    except IOError:
        pass


def fetch_og_metadata(url: str) -> Dict:
    """Fetch Open Graph metadata from a URL."""
    metadata = {
        'url': url,
        'title': urlparse(url).netloc,
        'description': '',
        'image': '',
        'site_name': urlparse(url).netloc
    }

    # Check cache first
    cached = load_from_cache(url)
    if cached:
        return cached

    if not HAS_DEPENDENCIES:
        return metadata

    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract OG metadata
        og_title = soup.find('meta', property='og:title')
        og_desc = soup.find('meta', property='og:description')
        og_image = soup.find('meta', property='og:image')
        og_site = soup.find('meta', property='og:site_name')

        # Fallback to standard meta tags
        if og_title:
            metadata['title'] = og_title.get('content', metadata['title'])
        else:
            title_tag = soup.find('title')
            if title_tag:
                metadata['title'] = title_tag.get_text(strip=True)

        if og_desc:
            metadata['description'] = og_desc.get('content', '')
        else:
            desc_tag = soup.find('meta', attrs={'name': 'description'})
            if desc_tag:
                metadata['description'] = desc_tag.get('content', '')

        if og_image:
            metadata['image'] = og_image.get('content', '')

        if og_site:
            metadata['site_name'] = og_site.get('content', metadata['site_name'])

        # Save to cache
        save_to_cache(url, metadata)

    except Exception as e:
        print(f"[link_preview] Failed to fetch metadata for {url}: {e}")

    return metadata


def generate_card_html(metadata: Dict) -> str:
    """Generate HTML for a link preview card."""
    title = metadata.get('title', metadata['url'])
    description = metadata.get('description', '')
    image = metadata.get('image', '')
    url = metadata['url']
    site_name = metadata.get('site_name', urlparse(url).netloc)

    # Truncate description if too long
    if len(description) > 150:
        description = description[:147] + '...'

    image_html = ''
    if image:
        image_html = f'''
        <div class="link-preview-image">
            <img src="{image}" alt="{title}" loading="lazy">
        </div>'''

    return f'''
<div class="link-preview-card">
    <a href="{url}" target="_blank" rel="noopener noreferrer">
        {image_html}
        <div class="link-preview-content">
            <div class="link-preview-title">{title}</div>
            <div class="link-preview-description">{description}</div>
            <div class="link-preview-url">{site_name}</div>
        </div>
    </a>
</div>
'''


def replace_preview_blocks(match: re.Match) -> str:
    """Replace a preview code block with card HTML."""
    url = match.group(1).strip()
    metadata = fetch_og_metadata(url)
    return generate_card_html(metadata)


def on_page_markdown(markdown: str, **kwargs) -> str:
    """MkDocs hook: Process markdown content."""
    return PREVIEW_PATTERN.sub(replace_preview_blocks, markdown)
