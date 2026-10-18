# ==============================================================================
# FILE: src/domain/value_objects/match_score.py
# LAYER: Domain (Value Objects)
#
# WHY WE NEED THIS FILE:
# - Encapsulates the suitability score (integer between 0 and 100) comparing a
#   candidate's profile against a verified job post.
# - Enforces domain invariant rules (e.g. score cannot be negative or > 100).
# - Stores structured breakdown: matching_skills, missing_skills, and seniority_fit.
# ==============================================================================
