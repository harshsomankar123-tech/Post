# ==============================================================================
# FILE: src/application/ports/search_harvester_port.py
# LAYER: Application (Ports / Interfaces)
#
# WHY WE NEED THIS FILE:
# - Defines the abstract contract (Protocol) for searching public search engines.
# - Decouples our application logic from any specific search tool (DuckDuckGo, Brave, etc.).
# - If we change search providers in the future, our application code remains untouched.
# ==============================================================================
