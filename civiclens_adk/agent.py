from google.adk.agents.llm_agent import Agent

from .subagents.security_agent import security_agent
from .subagents.document_agent import document_agent
from .subagents.deadline_agent import deadline_agent
from .subagents.eligibility_agent import eligibility_agent
from .subagents.action_agent import action_agent
from .subagents.memory_agent import memory_agent
from .subagents.reminder_agent import reminder_agent

root_agent = Agent(
    name="civiclens_coordinator",
    model="gemini-2.5-flash",

    description="Coordinates document intelligence agents.",

    instruction="""
    You are CivicLens AI.

    Delegate work to specialized agents.

    Security Agent:
    Check for unsafe content.

    Document Agent:
    Summarize the document.

    Deadline Agent:
    Extract dates and deadlines.

    Eligibility Agent:
    Extract requirements.

    Action Agent:
    Create a checklist.

    Combine all outputs into a final report.
    """,

    sub_agents=[
        security_agent,
        document_agent,
        deadline_agent,
        eligibility_agent,
        action_agent,
        memory_agent,
        reminder_agent
    ]
)
