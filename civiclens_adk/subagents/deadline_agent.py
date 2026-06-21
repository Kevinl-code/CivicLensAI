from google.adk.agents.llm_agent import Agent
from ..tools.date_tool import find_dates

deadline_agent = Agent(
    name="deadline_agent",
    model="gemini-2.5-flash",
    instruction="""
    Extract important dates and deadlines.
    Always use the available tool.
    """,
    tools=[find_dates]
)