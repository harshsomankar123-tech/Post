# ==============================================================================
# FILE: src/application/ports/resume_parser_port.py
# LAYER: Application (Ports / Interfaces)
#
# WHY WE NEED THIS FILE:
# - Defines the abstract contract for converting an uploaded resume file (PDF/DOCX)
#   into a structured CandidateProfile entity.
# - Isolates file format handling (PyPDF, pdfplumber, OCR) from the business domain.
# ==============================================================================
