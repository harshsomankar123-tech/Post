# ==============================================================================
# FILE: src/presentation/api/routes.py
# LAYER: Presentation (HTTP & Streaming Controllers)
#
# WHY WE NEED THIS FILE:
# - Defines HTTP endpoints:
#   1. POST /api/v1/resume/upload: Uploads and parses candidate resume.
#   2. POST /api/v1/jobs/search: Triggers the harvesting and matching pipeline.
#   3. GET /api/v1/jobs/stream: Streams live LangGraph progress to the UI via SSE.
# ==============================================================================
