# ==============================================================================
# FILE: src/infrastructure/harvesting/date_normalizer.py
# LAYER: Infrastructure (Harvesters)
#
# WHY WE NEED THIS FILE:
# - Normalizes fuzzy human time strings ("3 hours ago", "yesterday", "1 month ago")
#   into standard UTC datetime objects.
# - Enables deterministic chronological sorting (newest posts first) on the feed.
# ==============================================================================
