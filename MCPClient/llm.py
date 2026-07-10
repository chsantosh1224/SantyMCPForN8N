from ollama import AsyncClient

class QwenLLM:

    def __init__(self):
        self.client = AsyncClient(host="http://localhost:11434")
        self.model = "qwen2.5:7b"

    async def chat(self, prompt: str):

        response = await self.client.chat(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response["message"]["content"]