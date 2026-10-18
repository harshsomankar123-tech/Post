# ==============================================================================
# FILE: src/infrastructure/harvesting/query_builder.py
# LAYER: Infrastructure (Harvesters)
#
# WHY WE NEED THIS FILE:
# - Constructs high-recall search engine dorks targeting public LinkedIn posts.
# - Combines target roles with hiring signals (e.g. 'site:linkedin.com "hiring" "SDE"').
# - Prevents over-constraining the search engine so no relevant posts are missed.
# ==============================================================================
