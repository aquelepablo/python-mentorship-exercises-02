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

def normalize_text_without_accents_and_special_chars(text: str) -> str:
    """
    Normalize text by removing accents, punctuation, and special characters,
    keeping only letters, numbers, and spaces.
    """

    normalized_text = text.strip().lower()
    normalized_text = unicodedata.normalize("NFD", normalized_text)
    normalized_text = "".join(
        char
        for char in normalized_text
        # Remove accents, punctuation, symbols and special characters, keeping only letters, numbers, and spaces
        if not unicodedata.combining(char) 
        and (unicodedata.category(char)[0] in ("L", "N") or char == " ")
    )

    return normalized_text

def normalize_number(value: str, digits: int = None) -> float | None:
    """
    Normalize a number string that may use '.' as thousands separator
    and ',' as decimal separator, returning a float.
    """
    value = value.strip()

    if not value:
        return None

    if "." in value and "," in value:
        value = value.replace(".", "")

    if "," in value:
        value = value.replace(",", ".")

    try:
        return_value = float(value)
    except Exception as e:
        return None

    if digits:
        return_value = round(return_value, digits)
    
    return return_value

    