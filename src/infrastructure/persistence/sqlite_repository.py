# ==============================================================================
# FILE: src/infrastructure/persistence/sqlite_repository.py
# LAYER: Infrastructure (Persistence)
#
# WHY WE NEED THIS FILE:
# - Implements the IPostRepository port using Python's built-in sqlite3.
# - Stores seen post URL hashes to ensure permanent deduplication across runs.
# - Stores user profiles and saved opportunities with $0 cost, zero servers, and zero Redis.
# ==============================================================================
