# ==============================================================================
# FILE: src/domain/entities/verified_job.py
# LAYER: Domain (Entities)
#
# WHY WE NEED THIS FILE:
# - Represents a post that has successfully passed the Classifier and is confirmed
#   to be a genuine job or internship vacancy (not course ads or celebration spam).
# - Stores structured business entities: role_title, company_name, experience_required,
#   recruiter_email, application_link, and clean_post_text.
# - Used by the matching engine to compare against candidate skills.
# ==============================================================================
