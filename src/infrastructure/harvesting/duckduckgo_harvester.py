import time
from typing import List, Dict, Any
from ddgs import DDGS
from src.application.ports.search_harvester_port import ISearchHarvester
from src.domain.value_objects.time_filter import TimeFilter

class DuckDuckGoSearchHarvester:
    """Implements ISearchHarvester using DDGS public search index with adaptive fallback."""

    def __init__(self, request_delay: float = 0.5):
        self.request_delay = request_delay

    def harvest(
        self,
        query: str,
        time_filter: TimeFilter = None,
        max_results: int = 50
    ) -> List[Dict[str, Any]]:
        """
        Fetches public search results paginated up to max_results without login.
        Attempts time-bounded search first; if empty, falls back to broad search
        so the application layer can normalize and filter timestamps locally.
        """
        results: List[Dict[str, Any]] = []

        try:
            with DDGS() as ddgs:
                # 1. Try with time filter if provided
                timelimit_val = time_filter.value if time_filter else None
                try:
                    raw_iterator = ddgs.text(
                        query,
                        timelimit=timelimit_val,
                        max_results=max_results
                    )
                    for item in raw_iterator:
                        results.append({
                            "title": item.get("title", ""),
                            "href": item.get("href", ""),
                            "body": item.get("body", "")
                        })
                except Exception:
                    results = []

                # 2. Resilient Fallback: If time-bounded query yielded 0 results, query broad
                if not results:
                    raw_iterator = ddgs.text(query, max_results=max_results)
                    for item in raw_iterator:
                        results.append({
                            "title": item.get("title", ""),
                            "href": item.get("href", ""),
                            "body": item.get("body", "")
                        })

            if self.request_delay > 0:
                time.sleep(self.request_delay)

        except Exception as e:
            print(f"[Harvester Notice] Query '{query}': {e}")

        return results
