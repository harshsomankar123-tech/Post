# ==============================================================================
# FILE: src/application/dtos/job_feed_dto.py
# LAYER: Application (Data Transfer Objects)
#
# WHY WE NEED THIS FILE:
# - Standardizes the exact JSON payload returned to the frontend UI dashboard.
# - Formats post cards with: author_name, post_url, relative_time ("2h ago"),
#   role_title, company_name, match_percentage, recruiter_email, and cold_pitch.
# - Ensures the UI only receives display-ready, sanitized data.
# ==============================================================================
