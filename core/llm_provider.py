class OpenAILLM:

    def __init__(self, model="gpt-4.1-mini"):
        try:
            from openai import OpenAI
        except ImportError as exc:
            raise ImportError(
                "OpenAI SDK is not installed. Run: uv add openai"
            ) from exc

        self.client = OpenAI()
        self.model = model

    def invoke(self, prompt):
        response = self.client.responses.create(
            model=self.model,
            input=prompt,
        )

        return response.output_text
