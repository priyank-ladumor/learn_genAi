import os
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PATH = os.path.join(BASE_DIR, "..", "..", "notes", "langchain_note.pdf")

# Normalize the path (removes ".." parts)
PATH = os.path.abspath(PATH)

loader = PyPDFLoader(PATH)

docs = loader.load()

splitter = CharacterTextSplitter(
    chunk_size=800,
    chunk_overlap=0,
    separator=''
)

result = splitter.split_documents(docs)

print(result[1].page_content)

'''
separator 
'''