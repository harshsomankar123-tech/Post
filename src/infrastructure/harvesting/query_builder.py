from typing import List

class LinkedInQueryBuilder:
    """Builds clean, high-recall search queries targeting public LinkedIn posts and listings."""

    @classmethod
    def build_hiring_queries(
        cls,
        target_roles: List[str],
        custom_keywords: List[str] = None
    ) -> List[str]:
        """
        Generates targeted search queries without over-constraining the search engine.
        """
        if not target_roles:
            target_roles = ["intern"]

        queries = []
        kw_str = f' "{custom_keywords[0]}"' if custom_keywords and custom_keywords[0] else ""

        for role in target_roles:
            # Query 1: Direct LinkedIn hiring posts & listings
            queries.append(f'site:linkedin.com "hiring" "{role}"{kw_str}')

        return list(dict.fromkeys(queries))
