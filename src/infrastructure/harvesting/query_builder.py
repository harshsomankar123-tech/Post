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
        Format: site:linkedin.com hiring {role} {keywords}
        """
        if not target_roles:
            target_roles = ["intern"]

        queries = []
        kw_str = f" {' '.join(custom_keywords)}" if custom_keywords else ""

        for role in target_roles:
            role_clean = role.strip().replace('"', '')
            # Clean natural query format for maximum recall
            queries.append(f"site:linkedin.com hiring {role_clean}{kw_str}".strip())

        return list(dict.fromkeys(queries))
