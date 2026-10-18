# ==============================================================================
# FILE: src/application/use_cases/classify_posts_use_case.py
# LAYER: Application (Use Cases)
#
# WHY WE NEED THIS FILE:
# - Takes a batch of RawPostItem entities from the harvester.
# - Sends them to the IPostClassifier port (System 1).
# - Discards non-hiring noise (bootcamps, celebration updates, advice).
# - Converts accepted posts into VerifiedJob entities with role, company, and email.
# ==============================================================================
