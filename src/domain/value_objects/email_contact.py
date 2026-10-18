# ==============================================================================
# FILE: src/domain/value_objects/email_contact.py
# LAYER: Domain (Value Objects)
#
# WHY WE NEED THIS FILE:
# - Validates and normalizes extracted recruiter email addresses.
# - Rejects malformed strings and spam handles (e.g. invalid domains).
# - Ensures only valid RFC-compliant emails reach the notification and UI layer.
# ==============================================================================
