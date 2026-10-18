# ==============================================================================
# FILE: src/infrastructure/harvesting/duckduckgo_harvester.py
# LAYER: Infrastructure (Harvesters)
#
# WHY WE NEED THIS FILE:
# - Implements the ISearchHarvester port using the free DDGS library.
# - Fetches paginated batches of public LinkedIn results without needing a login account.
# - Implements polite rate-limit delays and adaptive search fallbacks.
# ==============================================================================
