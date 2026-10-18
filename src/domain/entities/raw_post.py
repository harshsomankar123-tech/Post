from dataclasses import dataclass
from datetime import datetime
from typing import Optional

@dataclass(frozen=True)
class RawPostItem:
    """Core domain entity representing an unclassified, harvested post from LinkedIn."""
    post_id: str
    canonical_url: str
    author_name: str
    raw_snippet: str
    published_at_utc: Optional[datetime]
    relative_time_display: str
    original_title: str
