import re

def extract_dates(text):
    patterns = [
        r"\b\d{1,2}[/-]\d{1,2}[/-]\d{2,4}\b",
        r"\b\d{1,2}\s(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\s\d{4}\b",
        r"\b(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\s\d{1,2},\s\d{4}\b",
        r"\b\d{1,2}\s(?:January|February|March|April|May|June|July|August|September|October|November|December)\s\d{4}\b",
        r"\b\d{4}-\d{2}-\d{2}\b"
    ]

    dates = []

    for pattern in patterns:
        matches = re.findall(pattern, text, flags=re.IGNORECASE)
        dates.extend(matches)

    return list(set(dates))