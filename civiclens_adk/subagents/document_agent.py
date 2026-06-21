from google.adk.agents.llm_agent import Agent

document_agent = Agent(
    name="document_agent",
    model="gemini-2.5-flash",

    description="Analyzes government notices and circulars.",

    instruction="""
    Determine:

    1. Document type
    2. Purpose
    3. Summary

    Keep response concise.
    """
)