from agents.document_agent import DocumentAgent
from agents.deadline_agent import DeadlineAgent
from agents.eligibility_agent import EligibilityAgent
from agents.action_agent import ActionAgent
from agents.memory_agent import MemoryAgent
from agents.security_agent import SecurityAgent
from skills.summarizer import summarize_text


class RootAgent:

    def __init__(self):

        self.document_agent = DocumentAgent()
        self.deadline_agent = DeadlineAgent()
        self.eligibility_agent = EligibilityAgent()
        self.action_agent = ActionAgent()
        self.memory_agent = MemoryAgent()
        self.security_agent = SecurityAgent()

    def process_document(self, file_path):

        text = self.document_agent.extract_text(file_path)

        security = self.security_agent.validate(text)

        if not security["safe"]:

            return {
                "error": security["reason"]
            }

        summary = summarize_text(text)

        deadline_info = self.deadline_agent.analyze(text)

        eligibility_info = self.eligibility_agent.analyze(text)

        action_plan = self.action_agent.generate_plan(
            summary,
            deadline_info["dates"]
        )

        result = {
            "summary": summary,
            "dates": deadline_info["dates"],
            "eligibility": eligibility_info,
            "action_plan": action_plan
        }

        self.memory_agent.save(result)

        return result