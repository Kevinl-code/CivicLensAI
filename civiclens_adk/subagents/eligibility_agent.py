from google.adk.agents.llm_agent import Agent

from ..tools.eligibility_tool import check_eligibility

eligibility_agent = Agent(
    name="eligibility_agent",
    model="gemini-2.5-flash",

    description="Extracts eligibility requirements.",

    instruction="""
    Identify:

    - Required documents
    - Academic requirements
    - Eligibility criteria

    Always use the provided tool.
    """,

    tools=[
        check_eligibility
    ]
)