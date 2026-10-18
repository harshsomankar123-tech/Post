# ==============================================================================
# FILE: src/infrastructure/ai/system2_pitch_drafter.py
# LAYER: Infrastructure (AI Adapters)
#
# WHY WE NEED THIS FILE:
# - Implements the IPitchGenerator port using deep reasoning (System 2 LLM).
# - Takes candidate skills and projects from CandidateProfile and matches them
#   against what the recruiter asked for in the post.
# - Drafts a polite, tailored 3-sentence application message ready to copy & paste.
# ==============================================================================
