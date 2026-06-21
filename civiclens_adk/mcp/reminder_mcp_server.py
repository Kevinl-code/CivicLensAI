from mcp.server.fastmcp import FastMCP

mcp = FastMCP("CivicLens Reminder Server")

@mcp.tool()
def create_reminder(deadline: str):
    """
    Create reminder for deadline.
    """
    return {
        "status": "created",
        "deadline": deadline
    }

if __name__ == "__main__":
    mcp.run()