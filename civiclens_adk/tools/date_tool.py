import re

def find_dates(text: str):
    """
    Extract dates from text.
    """

    patterns = [
        r"\b\d{1,2}[/-]\d{1,2}[/-]\d{2,4}\b",
        r"\b\d{1,2}\s(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\s\d{4}\b",
        r"\b(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\s\d{1,2},\s\d{4}\b"
    ]

    dates = []

    for pattern in patterns:
        matches = re.findall(pattern, text, flags=re.IGNORECASE)
        dates.extend(matches)

    return {
        "dates": list(set(dates))
    }