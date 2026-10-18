# ==============================================================================
# FILE: src/application/use_cases/score_and_rank_use_case.py
# LAYER: Application (Use Cases)
#
# WHY WE NEED THIS FILE:
# - Compares the CandidateProfile against all VerifiedJob posts.
# - Assigns a MatchScore (0-100) to each post based on skill alignment.
# - Invokes IPitchGenerator (System 2) to draft personalized 3-sentence application notes.
# - Sorts the final output by match relevance and recency for presentation.
# ==============================================================================
