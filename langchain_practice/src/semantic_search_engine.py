"""
构建一个语义搜索系统
所需模块：pypdf langchain-community faiss-cpu
pip install pypdf langchain-community
"""
import asyncio
from langchain_core.documents import Document
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS


file_path = "DeepSeek_R1.pdf"
loader = PyPDFLoader(file_path)

docs = loader.load()





text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000, chunk_overlap=200, add_start_index=True
)


all_splits = text_splitter.split_documents(docs)


embeddings = OpenAIEmbeddings(model="text-embedding-3-large",
                              base_url="https://api.chatanywhere.tech",
                              api_key="sk-sNW6ZATAn03D6PPiN8I2KjI9X2gPBXjcnloWwz5L8VpWQaxQ")


vector_store = FAISS.from_documents(all_splits,embeddings)




result = vector_store.similarity_search("什么是MOE？")

for chunk in result:
    print(chunk.page_content,end="")

