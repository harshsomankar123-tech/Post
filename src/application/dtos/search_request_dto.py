# ==============================================================================
# FILE: src/application/dtos/search_request_dto.py
# LAYER: Application (Data Transfer Objects)
#
# WHY WE NEED THIS FILE:
# - Standardizes the input contract passed into use cases from API controllers.
# - Contains fields: target_roles (List[str]), custom_keywords (List[str]),
#   time_filter (str), and max_posts (int).
# - Keeps presentation/HTTP request validation separate from internal domain models.
# ==============================================================================
