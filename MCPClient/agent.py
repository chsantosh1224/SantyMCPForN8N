from llm import QwenLLM
import asyncio
from mcp_client import mcpclient as mcpc
from prompt import prompt1,UserRequest,FINAL_RESPONSE_PROMPT
import json
class agent_controller:
    def __init__(self,
                 llm: QwenLLM,
                 mcp_client: mcpc):

        self.llm = llm
        self.mcp = mcp_client

    async def process_requrest(self,Prompt):
        # Provide your exact N8N streamable endpoint URL
        mcpc_client1 = self.mcp
        llm_initialized=self.llm
        try:
            # Use 'async with' to manage the lifecycle of the connection
            async with mcpc_client1.connect() as session:
                # Pass the active session straight into your operation methods
                response = await mcpc_client1.list_tools(session)

                # Start the string
                tools_string = ""

                for t in response.tools:
                    schema = t.inputSchema if isinstance(t.inputSchema, dict) else t.inputSchema.dict()
                    parameters = schema.get("required", [])
                    
                    # Build the block for this tool
                    tools_string += f"Tool Name: {t.name}\n\n"
                    tools_string += f"Description:\n{t.description}\n\n"
                    tools_string += "Parameters:\n"
                    for param in parameters:
                        tools_string += f"- {param}\n"
                    
                    # Add spacing between tools
                    tools_string += "\n"

                # --- FIXED INDENTATION: The code below is now OUTSIDE the for-loop ---
                Prompt = UserRequest
                    
                await asyncio.sleep(1)
                # print(tools_string)
                
                # Formats your prompt template cleanly
                final_prompt=prompt1.replace("{tools_list}", tools_string).replace("{user_prompt}", Prompt)
                print(final_prompt)
                
                llm_response=await llm_initialized.chat(final_prompt)
                
                parsed_response = json.loads(llm_response)

                tools = parsed_response["tools"]
                tool_results = []
                for tool_call in tools:

                    tool = tool_call["tool"]
                    arguments = tool_call["arguments"]
                    print(f"\nCalling the tool {tool}")

                    result = await self.mcp.call_tool(
                        tool,
                        arguments
                    )

                    tool_results.append({
                        "tool": tool_call["tool"],
                        "result": result.structuredContent["result"]
                    })
                tool_results_json = json.dumps(tool_results, indent=2)
                final_prompt2=FINAL_RESPONSE_PROMPT.replace("{tool_results}", tool_results_json).replace("{user_prompt}", Prompt)
                llm_final_response=await llm_initialized.chat(final_prompt2)
                print("LLM Final response is : ")
                print(llm_final_response)    
                                
        except Exception as e:
            # If it's a TaskGroup error, extract the real underlying exception(s)
            if hasattr(e, 'exceptions'):
                print("❌ TaskGroup Errors:")
                for sub_err in e.exceptions:
                    print(f"  - {type(sub_err).__name__}: {sub_err}")
                    # Print the full traceback for the sub-error if needed
                    import traceback
                    traceback.print_exception(type(sub_err), sub_err, sub_err.__traceback__)
            else:
                print(f"❌ An error occurred during runtime: {e}")


