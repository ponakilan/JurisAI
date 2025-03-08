import faiss
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings


class VectorDB:
    def __init__(self):
        embeddings = OpenAIEmbeddings(
            model="text-embedding-3-large",
            api_key="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"
        )

        index = faiss.IndexFlatL2(len(embeddings.embed_query("hello world")))
        self.vector_store = FAISS.load_local(
            "case_index", embeddings, allow_dangerous_deserialization=True
        )

    def search(self, text, k):
        docs = self.vector_store.similarity_search(text, k=k)

        for doc in docs:
            print(doc.metadata)

        return docs
