"""
Module for text normalization and processing functions.
"""

from typing import List
import unicodedata

"""
To remove also special characters in this function you should use unicodedata.category(char) to check if the character is a letter or a number, for example: 
"""

def normalize_text_without_accent(text: str) -> str:
    """
    Normalize a text by removing accents and converting to lowercase.
    """

    normalized_text = text.strip().lower()
    normalized_text = unicodedata.normalize("NFD", normalized_text)
    normalized_text = "".join(
        char 
        for char in normalized_text 
        # Remove accents but keep special characters
        if not unicodedata.combining(char)
    )

    return normalized_text

def normalize_text_without_accent_and_special_chars(text: str) -> str:
    """
    Normalize a text by removing accents, special characters, and converting to lowercase.
    """

    normalized_text = text.strip().lower()
    normalized_text = unicodedata.normalize("NFD", normalized_text)
    normalized_text = "".join(
        char
        for char in normalized_text
        # Remove accents and special characters, keeping only letters and numbers
        if not unicodedata.combining(char) and unicodedata.category(char)[0] in ("L", "N")
    )

    return normalized_text
