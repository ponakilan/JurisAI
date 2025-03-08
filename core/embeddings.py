from openai import OpenAI, OpenAIError


class Embeddings:
    def __init__(self, client: OpenAI=None):
        self.client = client
        if not client:
            try:
                self.client = client = OpenAI()
            except OpenAIError:
                print("Please setup the environment by executing 'core/setup.py'.")

    def get_embeddings(self, text: str) -> list[float]:
        response = self.client.embeddings.create(
            input=text,
            model="text-embedding-3-small"
        )
        return response.data[0].embedding
