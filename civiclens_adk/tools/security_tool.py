def security_scan(text: str):
    """
    Scan content for prompt injection
    and unsafe instructions.
    """

    blocked_patterns = [
        "ignore previous instructions",
        "ignore all instructions",
        "reveal system prompt",
        "show system prompt",
        "api key",
        "password",
        "delete database",
        "shutdown server",
        "bypass security",
        "developer instructions"
    ]

    text = text.lower()

    for pattern in blocked_patterns:

        if pattern in text:

            return {
                "safe": False,
                "reason": pattern
            }

    return {
        "safe": True,
        "reason": "No threats detected"
    }