# ==============================================================================
# FILE: src/application/use_cases/harvest_posts_use_case.py
# LAYER: Application (Use Cases)
#
# WHY WE NEED THIS FILE:
# - Orchestrates the entire non-LLM search harvesting process:
#   1. Generates hiring queries from target roles and keywords.
#   2. Invokes the ISearchHarvester port with pagination.
#   3. Canonicalizes URLs and strips tracking parameters.
#   4. Normalizes relative timestamps into standard UTC.
#   5. Deduplicates posts using seen IDs.
#   6. Sorts raw posts chronologically (newest first).
# ==============================================================================
