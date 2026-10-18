# ==============================================================================
# FILE: src/infrastructure/ai/pypdf_resume_parser.py
# LAYER: Infrastructure (AI Adapters)
#
# WHY WE NEED THIS FILE:
# - Implements the IResumeParser port.
# - Reads raw binary PDF files from local upload using PyPDF.
# - Cleans and normalizes the extracted text so the LLM can parse candidate skills.
# ==============================================================================
