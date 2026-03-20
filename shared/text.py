"""
Module for text normalization and processing functions.
"""

from typing import List
import unicodedata

def normalize_text_without_accent(text: str) -> str:
    """
    Normalize a text by removing accents and converting to lowercase.
    """

    normalized_text = text.strip().lower()
    normalized_text = unicodedata.normalize("NFD", normalized_text)
    normalized_text = "".join(char for char in normalized_text if not unicodedata.combining(char))

    return normalized_text