import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from src.domain.value_objects.time_filter import TimeFilter
from src.infrastructure.harvesting.duckduckgo_harvester import DuckDuckGoSearchHarvester
from src.application.use_cases.harvest_posts_use_case import HarvestPostsUseCase

def main():
    print("=" * 70)
    print("🚀 TESTING LINKEDIN SEARCH HARVESTER (CLEAN ARCHITECTURE - NO LLM)")
    print("=" * 70)

    # 1. Initialize Harvester
    harvester = DuckDuckGoSearchHarvester(request_delay=0.5)

    # 2. Initialize Application Use Case (Clean Architecture Dependency Injection)
    use_case = HarvestPostsUseCase(harvester=harvester)

    # 3. Define Criteria
    target_roles = ["intern"]

    print(f"🎯 Target Roles:   {target_roles}")
    print("\n🔍 Fetching & paginating public LinkedIn posts without login...\n")

    posts = use_case.execute(
        target_roles=target_roles,
        max_total_posts=5
    )

    print(f"✅ Total Unique LinkedIn Opportunities Harvested: {len(posts)}\n")

    for idx, post in enumerate(posts, 1):
        print(f"[{idx}] 👤 Author/Company: {post.author_name}")
        print(f"    🕒 Timestamp:      {post.relative_time_display} (UTC: {post.published_at_utc})")
        print(f"    🔗 Canonical URL:  {post.canonical_url}")
        print(f"    📝 Text Snippet:   {post.raw_snippet[:150]}...")
        print("-" * 70)

if __name__ == "__main__":
    main()
