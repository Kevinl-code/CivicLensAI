from google.adk.agents.llm_agent import Agent

reminder_agent = Agent(
    name="reminder_agent",
    model="gemini-2.5-flash",

    description="Creates reminders using MCP services.",

    instruction="""
    Create reminders whenever deadlines are found.

    Use MCP reminder services.
    """
)