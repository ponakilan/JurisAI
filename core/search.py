import faiss
import streamlit as st
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings


class VectorDB:
    def __init__(self):
        embeddings = OpenAIEmbeddings(
            model="text-embedding-3-large",
            api_key=st.secrets['OPENAI_API_KEY']
        )

        index = faiss.IndexFlatL2(len(embeddings.embed_query("hello world")))
        self.vector_store = FAISS.load_local(
            "case_index", embeddings, allow_dangerous_deserialization=True
        )

    def search(self, text, k):
        docs = self.vector_store.similarity_search(text, k=k)
        return docs
