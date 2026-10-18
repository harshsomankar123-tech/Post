# ==============================================================================
# FILE: src/domain/value_objects/time_filter.py
# LAYER: Domain (Value Objects)
#
# WHY WE NEED THIS FILE:
# - An immutable Enum representing allowed search time horizons:
#   PAST_24H ("d"), PAST_WEEK ("w"), PAST_MONTH ("m").
# - Prevents invalid string inputs across the entire application and maps cleanly
#   to search engine time operators.
# ==============================================================================
