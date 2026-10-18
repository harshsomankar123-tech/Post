# ==============================================================================
# FILE: src/domain/entities/candidate_profile.py
# LAYER: Domain (Entities)
#
# WHY WE NEED THIS FILE:
# - Represents the structured candidate profile extracted from their uploaded resume.
# - Stores core attributes: candidate_id, primary_skills (e.g. Python, FastAPI, Docker),
#   experience_level (e.g. Fresher / Intern / 1-2 years), and inferred target roles.
# - Serves as the single source of truth for all downstream matchmaking logic.
# ==============================================================================
