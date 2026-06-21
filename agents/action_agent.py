from google import genai
import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

class ActionAgent:

    def generate_plan(self, summary, dates):

        prompt = f"""
        Create an action plan.

        Summary:
        {summary}

        Dates:
        {dates}

        Return:
        Step 1
        Step 2
        Step 3
        """

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text