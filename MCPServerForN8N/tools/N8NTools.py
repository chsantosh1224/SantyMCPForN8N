import requests
    
webhook_summary_url = "https://chsantosh1224.app.n8n.cloud/webhook-test/summarize-email"
webhook_ask_question= "https://chsantosh1224.app.n8n.cloud/webhook-test/ask-text"

def register_tools(mcp):
        
    @mcp.tool
    def summarizeEmail(subject,email_body)   ->str:
                """
                Summarize an email using the n8n AI workflow.
                """
                data_to_send = {        'subject': subject, 'email_body': email_body}
                response=requests.post(webhook_summary_url,data_to_send)
                print(response)
                data_list=response.json()
                print('summarized data is ')
                email_data = data_list[0]
                return (email_data['summary'])

    @mcp.tool    
    def askQuestion(text,question) ->str:
                """
                Ask a question from the below context.
                """
    @mcp.tool
    def askQuestion(text: str, question: str) -> str:
        """
                Ask a question from the below context.
                """
        try:
            print("Entered askQuestion")

            data_to_send = {
                "text": text,
                "question": question
            }

            print("Sending:", data_to_send)

            response = requests.post(
                webhook_ask_question,
                data=data_to_send,
                timeout=30
            )

            print("Status:", response.status_code)
            print("Body:", response.text)

            
            data = response.json()
            return data["answer"]

        except Exception:
            import traceback

            traceback.print_exc()

            raise
                        
  #  mcp.add_tool(summarizeEmail)
  #  mcp.add_tool(askQuestion)            