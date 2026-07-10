import os
import sys
from fastmcp import FastMCP
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from tools.N8NTools import register_tools


mcp = FastMCP("N8N MCP Server")



register_tools(mcp)
print("Registered tools:")



if __name__ == "__main__":
    mcp.run(
    transport="streamable-http",
    host="127.0.0.1",
    port=8000
)
