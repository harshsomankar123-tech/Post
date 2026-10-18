import re
from typing import List, Set
from src.domain.entities.raw_post import RawPostItem
from src.domain.value_objects.time_filter import TimeFilter
from src.application.ports.search_harvester_port import ISearchHarvester
from src.infrastructure.harvesting.query_builder import LinkedInQueryBuilder
from src.infrastructure.harvesting.url_cleaner import LinkedInUrlCleaner
from src.infrastructure.harvesting.date_normalizer import DateNormalizer

class HarvestPostsUseCase:
    """
    Application Use Case that coordinates:
    1. Query formulation
    2. Zero-auth harvesting & pagination
    3. URL canonicalization and deduplication
    4. Date normalization
    5. Chronological sorting
    """

    def __init__(self, harvester: ISearchHarvester):
        self._harvester = harvester

    def execute(
        self,
        target_roles: List[str],
        custom_keywords: List[str] = None,
        time_filter: TimeFilter = None,
        max_total_posts: int = 15
    ) -> List[RawPostItem]:
        """
        Executes end-to-end harvesting and returns deduplicated, chronologically sorted posts.
        """
        queries = LinkedInQueryBuilder.build_hiring_queries(target_roles, custom_keywords)
        seen_ids: Set[str] = set()
        harvested_posts: List[RawPostItem] = []

        per_query_limit = max(5, max_total_posts // max(1, len(queries)))

        for query in queries:
            if len(harvested_posts) >= max_total_posts:
                break

            raw_items = self._harvester.harvest(
                query=query,
                time_filter=time_filter,
                max_results=per_query_limit
            )

            for item in raw_items:
                raw_url = item.get("href", "")
                if "linkedin.com" not in raw_url:
                    continue

                canonical_url, post_id, author_hint = LinkedInUrlCleaner.clean(raw_url)

                # Deduplicate by post_id
                if post_id in seen_ids:
                    continue
                seen_ids.add(post_id)

                title = item.get("title", "")
                body = item.get("body", "")

                # Extract author name from title if available (e.g. "John Doe on LinkedIn: ...")
                author_name = author_hint
                author_match = re.search(r'^(.*?)\s+(?:on\s+LinkedIn|hiring|is\s+Hiring):', title, re.IGNORECASE)
                if author_match:
                    author_name = author_match.group(1).strip()

                published_at_utc, relative_display = DateNormalizer.parse_date(body)

                post = RawPostItem(
                    post_id=post_id,
                    canonical_url=canonical_url,
                    author_name=author_name or "LinkedIn Recruiter",
                    raw_snippet=body,
                    published_at_utc=published_at_utc,
                    relative_time_display=relative_display,
                    original_title=title
                )

                harvested_posts.append(post)

        # Sort chronologically (newest first)
        harvested_posts.sort(
            key=lambda p: p.published_at_utc.timestamp() if p.published_at_utc else 0,
            reverse=True
        )

        return harvested_posts
