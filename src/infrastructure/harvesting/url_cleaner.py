# ==============================================================================
# FILE: src/infrastructure/harvesting/url_cleaner.py
# LAYER: Infrastructure (Harvesters)
#
# WHY WE NEED THIS FILE:
# - Cleans tracking parameters (?utm_source=..., &rcm=...) from raw LinkedIn links.
# - Derives the permanent canonical URL and unique post ID for deduplication.
# - Extracts author handle hints from URL slugs.
# ==============================================================================
