class SecurityAgent:

    BLOCKED_PATTERNS = [
        "ignore previous instructions",
        "system prompt",
        "delete database",
        "shutdown server",
        "reveal secrets",
        "api key"
    ]

    def validate(self, text):

        lowered = text.lower()

        for pattern in self.BLOCKED_PATTERNS:

            if pattern in lowered:

                return {
                    "safe": False,
                    "reason": pattern
                }

        return {
            "safe": True
        }