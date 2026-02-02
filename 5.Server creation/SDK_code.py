import asyncio
from typing import Any, Dict, List

import mcp.server.stdio
import mcp.types as types
from mcp.server.lowlevel import Server, NotificationOptions
from mcp.server.models import InitializationOptions

# Create MCP server
server = Server("demo-sdk")

# =========================
# 1) List available tools
# =========================
@server.list_tools()
async def list_tools() -> List[types.Tool]:
    return [
        types.Tool(
            name="add",
            description="Add two numbers",
            inputSchema={
                "type": "object",
                "properties": {
                    "a": {"type": "number"},
                    "b": {"type": "number"}
                },
                "required": ["a", "b"]
            },
        )
    ]


# =========================
# 2) Handle tool calls
# =========================
@server.call_tool()
async def call_tool(name: str, arguments: Dict[str, Any]) -> List[types.TextContent]:
    if name == "add":
        a = arguments.get("a", 0)
        b = arguments.get("b", 0)
        result = a + b
        return [types.TextContent(type="text", text=str(result))]

    return [types.TextContent(type="text", text=f"Unknown tool: {name}")]


# =========================
# 3) Run MCP server (STDIO)
# =========================
async def main():
    async with mcp.server.stdio.stdio_server() as (read, write):
        await server.run(
            read,
            write,
            InitializationOptions(
                server_name="demo-sdk",
                server_version="1.0.0",
                capabilities=server.get_capabilities(
                    notification_options=NotificationOptions(),
                    experimental_capabilities={},
                ),
            ),
        )


if __name__ == "__main__":
    asyncio.run(main())
