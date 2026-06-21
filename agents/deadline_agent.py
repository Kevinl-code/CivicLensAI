from skills.date_extractor import extract_dates

class DeadlineAgent:

    def analyze(self, text):

        dates = extract_dates(text)

        return {
            "dates": dates
        }