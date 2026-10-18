# ==============================================================================
# FILE: src/application/ports/post_classifier_port.py
# LAYER: Application (Ports / Interfaces)
#
# WHY WE NEED THIS FILE:
# - Defines the abstract contract for the System 1 Classifier.
# - Takes raw post text and determines whether it represents a real hiring vacancy
#   or non-hiring noise (bootcamps, celebration updates, advice).
# - Decouples the decision logic from whether we use Gemini, Groq, or a local model.
# ==============================================================================
