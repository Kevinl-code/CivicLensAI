from agents.root_agent import RootAgent


def analyze_document(text: str):

    agent = RootAgent()

    result = {
        "summary": text[:500]
    }

    return result