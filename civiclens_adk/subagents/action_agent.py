from google.adk.agents.llm_agent import Agent

action_agent = Agent(
    name="action_agent",
    model="gemini-2.5-flash",

    description="Creates an action plan.",

    instruction="""
    Generate a checklist.

    Format:

    Step 1
    Step 2
    Step 3

    Include any deadlines if present.
    """
)