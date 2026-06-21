class EligibilityAgent:

    def analyze(self, text):

        text = text.lower()

        requirements = []

        keywords = [
            "ug",
            "pg",
            "bachelor",
            "master",
            "engineering",
            "income certificate",
            "marksheet",
            "aadhaar",
            "community certificate"
        ]

        for keyword in keywords:

            if keyword in text:
                requirements.append(keyword)

        return {
            "requirements": requirements
        }