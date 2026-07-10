prompt1="""You are an AI assistant.

You have access to the following tools.

Available Tools:

{tools_list}
-----------------------------------

Rules:
1. Choose one or more tools needed to satisfy the request.
2. Execute them in the correct order.
3. Extract all required arguments from the user's request.
4. Return ONLY valid JSON.
5. Do not explain your reasoning.

Return JSON in this format:

{
    "tools": [
        {
            "tool": "<tool_name>",
            "arguments": {
            }
        }
    ]
}
Return ONLY valid JSON.

Rules:
- Escape all newline characters as \n.
- Escape all quotes inside strings.
- Ensure the output is valid JSON that can be parsed by Python's json.loads().

User Request:
{user_prompt}"""

UserRequest="""Answer the following question and summarize the email.

Question:
Who is the point of contact?

Subject:
Leave Request

Email:
Hi Team,

I will be on leave tomorrow due to a personal emergency.
Please let me know if anything urgent needs my attention. Also I want to inform that I am blessed with a baby girl. I would like to opt for 2 weeks of paternity leave now.

I want to tell you that I will be assigning the task of logik.io to Rahul. Rahul will act as the point of contact. If you have any questions first reach out to Rahul and then me.

I will throw a party once I am back. Also, want to check if Anand has brought any sweets from USA? If yes, please keep some aside for me.

Love you all.
Take care!

Regards,
Santosh"""    

FINAL_RESPONSE_PROMPT="""You are an AI assistant.

The user originally asked:

{user_request}

The following tools have already been executed.

Tool Results:

{tool_results}

Instructions:

1. Use ONLY the tool results.
2. Do not invent information.
3. If multiple tools returned information, combine them into one coherent answer.
4. Produce a natural response.
"""