from ..tools.security_tool import security_scan

def security_skill(text: str):
    """
    Reusable security analysis skill.
    """

    return security_scan(text)