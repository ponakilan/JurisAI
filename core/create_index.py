import os
import getpass
from uuid import uuid4

import faiss
import tqdm
import PyPDF2
from langchain_community.docstore.in_memory import InMemoryDocstore
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain_core.documents import Document

files_path = "../data"

embeddings = OpenAIEmbeddings(
    model="text-embedding-3-large",
    api_key="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"
)

index = faiss.IndexFlatL2(len(embeddings.embed_query("hello world")))
print("Index created")
vector_store = FAISS(
    embedding_function=embeddings,
    index=index,
    docstore=InMemoryDocstore(),
    index_to_docstore_id={},
)

count = 0
for file in tqdm.tqdm(os.listdir(files_path)[:100]):
    try:
        reader = PyPDF2.PdfReader(f'{files_path}/{file}')
        content = " ".join([page.extract_text() for page in reader.pages])

        document = Document(
            page_content=content,
            metadata={"file_name": file}
        )
        uuid = [str(uuid4())]
        document = [document]

        vector_store.add_documents(
            documents=document,
            ids=uuid
        )
        count += 1
    except:
        continue
vector_store.save_local("case_index")
print(f"{count} embeddings saved.")
