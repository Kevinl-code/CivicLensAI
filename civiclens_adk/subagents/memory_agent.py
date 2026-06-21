from google.adk.agents.llm_agent import Agent

memory_agent = Agent(
    name="memory_agent",
    model="gemini-2.5-flash",

    description="Maintains long-term memory and stores extracted information.",

    instruction="""
    Analyze previous document findings and maintain memory.

    Tasks:
    - Remember important dates
    - Remember eligibility requirements
    - Remember action plans
    - Detect recurring opportunities

    Return concise memory summaries.
    """
)