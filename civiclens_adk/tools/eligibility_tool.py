def check_eligibility(text: str):
    """
    Extract eligibility requirements.
    """

    text = text.lower()

    requirements = []

    keywords = [
        "aadhaar",
        "marksheet",
        "income certificate",
        "community certificate",
        "transfer certificate",
        "ug",
        "pg",
        "undergraduate",
        "postgraduate",
        "bachelor",
        "master",
        "cgpa",
        "percentage"
    ]

    for keyword in keywords:

        if keyword in text:
            requirements.append(keyword)

    return {
        "requirements": requirements,
        "count": len(requirements)
    }