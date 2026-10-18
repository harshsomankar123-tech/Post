# ==============================================================================
# FILE: src/application/use_cases/parse_resume_use_case.py
# LAYER: Application (Use Cases)
#
# WHY WE NEED THIS FILE:
# - Coordinates reading the raw resume file (PDF) via the IResumeParser port.
# - Prompts the LLM to structure extracted skills, seniority, and recommended target roles.
# - Saves the candidate profile for subsequent searches.
# ==============================================================================
