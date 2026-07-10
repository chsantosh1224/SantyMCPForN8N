import asyncio
from contextlib import asynccontextmanager
from mcp import ClientSession
from mcp.client.streamable_http import streamable_http_client as sh

class mcpclient:
    def __init__(self, server_url: str):
        self.server_url = server_url

    @asynccontextmanager
    async def connect(self):
        """Asynchronous context manager that keeps the connection alive."""
        print(f"Connecting to N8N at {self.server_url}...")
        
        # Keep streams open for the duration of the context block
        async with sh(self.server_url) as (read_stream, write_stream, _):
            print("Creating MCP Client Session...")
            async with ClientSession(read_stream, write_stream) as session:
                print("Initializing connection protocol...")
                self.session = session
                await session.initialize()
                print("✅ Connected successfully to N8N Server!")
                
                # Yield the session to main.py
                yield session
                self.session = None 
                
        print("🔌 Connection safely closed and cleaned up.")

    async def list_tools(self, session: ClientSession):
        """Fetches tools using the active session passed from main.py."""
        try:
            print("\n--- Executing Operations While Connected ---")
            tools_response = await session.list_tools()
            
            return tools_response
        except Exception as e:
            print(f"❌ An error occurred during list_tools: {e}")

    async def call_tool(self, tool_name: str, arguments: dict):
        try:
            print(f"\nCalling tool: {tool_name}")

            result = await self.session.call_tool(
                tool_name,
                arguments
            )

            return result

        except Exception as ex:
            print(f"Error calling tool: {ex}")
            raise