
def normalize_whitespace(text: str) -> str:
    """Nahradí skupiny bílých znaků jednou mezerou."""
    return text.strip()

def count_words(text: str) -> int:
    """Vrátí počet slov oddělených bílými znaky."""
    return len(normalize_whitespace(text).split())