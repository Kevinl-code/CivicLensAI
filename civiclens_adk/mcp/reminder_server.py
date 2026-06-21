from mcp.server.fastmcp import FastMCP

mcp = FastMCP("CivicLensReminder")


@mcp.tool()
def set_reminder(date: str):

    return f"Reminder created for {date}"


if __name__ == "__main__":
    print("CivicLens MCP Running...")
    mcp.run()