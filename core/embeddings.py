from openai import OpenAI
import streamlit as st


class Embeddings:
    def __init__(self):
        self.client = OpenAI(
            api_key=st.secrets['OPENAI_API_KEY']
        )

    def get_embeddings(self, text: str) -> list[float]:
        response = self.client.embeddings.create(
            input=text,
            model="text-embedding-3-small"
        )
        return response.data[0].embedding
