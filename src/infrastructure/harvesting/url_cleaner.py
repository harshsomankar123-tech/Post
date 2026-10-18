import re
from urllib.parse import urlparse, urlunparse

class LinkedInUrlCleaner:
    """Cleans raw LinkedIn URLs, extracts canonical links, post IDs, and author handles."""

    @staticmethod
    def clean(raw_url: str) -> tuple[str, str, str]:
        """
        Cleans tracking parameters from a URL.
        Returns:
            canonical_url: Clean URL without query params or anchors.
            post_id: Unique identifier extracted from the URL.
            author_hint: Username or handle prefix extracted from URL slug.
        """
        parsed = urlparse(raw_url)
        # Strip all query params (?utm_source=...) and fragments (#...)
        canonical_url = urlunparse((parsed.scheme, parsed.netloc, parsed.path.rstrip("/"), "", "", ""))

        path_segments = [seg for seg in parsed.path.split("/") if seg]
        slug = path_segments[-1] if path_segments else ""

        # Extract numeric post ID if present in slug (e.g. activity-7508976174145019904)
        id_match = re.search(r'(\d{15,22})', slug)
        post_id = id_match.group(1) if id_match else slug

        # Extract author handle prefix before underscore (e.g. isumitsoni_hiring-share...)
        author_hint = ""
        if "_" in slug:
            author_hint = slug.split("_")[0]
        elif len(path_segments) >= 2:
            author_hint = path_segments[-2]

        return canonical_url, post_id, author_hint
