# ==============================================================================
# FILE: src/application/ports/post_repository_port.py
# LAYER: Application (Ports / Interfaces)
#
# WHY WE NEED THIS FILE:
# - Defines the abstract contract for storing and querying seen posts and application history.
# - Decouples our use cases from database technology (SQLite, PostgreSQL, or In-Memory).
# - Enables permanent deduplication so users never see the same post twice.
# ==============================================================================
