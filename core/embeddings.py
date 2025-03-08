from openai import OpenAI


class Embeddings:
    def __init__(self, client: OpenAI=None):
        self.client = client
        if not client:
            self.client = client = OpenAI()

    def get_embeddings(self, text: str) -> list[float]:
        response = self.client.embeddings.create(
            input=text,
            model="text-embedding-3-small"
        )
        return response.data[0].embedding
