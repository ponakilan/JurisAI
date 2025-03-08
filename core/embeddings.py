from openai import OpenAI


class Embeddings:
    def __init__(self):
        self.client = OpenAI(
            api_key="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"
        )

    def get_embeddings(self, text: str) -> list[float]:
        response = self.client.embeddings.create(
            input=text,
            model="text-embedding-3-small"
        )
        return response.data[0].embedding
