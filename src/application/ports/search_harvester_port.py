from typing import Protocol, List
from src.domain.entities.raw_post import RawPostItem
from src.domain.value_objects.time_filter import TimeFilter

class ISearchHarvester(Protocol):
    """Port interface for crawling public search index results."""

    def harvest(
        self,
        query: str,
        time_filter: TimeFilter,
        max_results: int
    ) -> List[dict]:
        """
        Executes a paginated search query.
        Returns a list of raw dictionaries containing {'title', 'href', 'body'}.
        """
        ...
