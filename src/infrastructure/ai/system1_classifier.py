# ==============================================================================
# FILE: src/infrastructure/ai/system1_classifier.py
# LAYER: Infrastructure (AI Adapters)
#
# WHY WE NEED THIS FILE:
# - Implements the IPostClassifier port using a fast, low-latency LLM (Gemini / Groq).
# - Uses LangChain structured output to evaluate raw post text:
#   1. Determines if the post is genuinely hiring (is_hiring: true/false).
#   2. Drops bootcamps, courses, and celebratory announcements.
#   3. Extracts role title, company name, and recruiter contact email.
# ==============================================================================
