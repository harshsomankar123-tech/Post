# ==============================================================================
# FILE: src/presentation/api/main.py
# LAYER: Presentation (API Entrypoint)
#
# WHY WE NEED THIS FILE:
# - The FastAPI application factory and server entrypoint.
# - Configures CORS middleware, life-cycle event handlers, and router inclusion.
# - Launched via: uvicorn src.presentation.api.main:app --reload
# ==============================================================================
