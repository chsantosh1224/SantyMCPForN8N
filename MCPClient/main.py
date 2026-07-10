import asyncio
from mcp_client import mcpclient as mcpc
from llm import QwenLLM
from agent import agent_controller
import json
from prompt import prompt1,UserRequest
import re


async def main():
    # Provide your exact N8N streamable endpoint URL
    mcpc_client1 = mcpc("http://127.0.0.1:8000/mcp")
    llm=QwenLLM()
    controller=agent_controller(llm,mcpc_client1)
    await controller.process_requrest(UserRequest)

if __name__ == "__main__":
    asyncio.run(main())