import os
from langchain_community.document_loaders import PyPDFLoader

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Go up two levels: document_loader -> 08_rag -> learn_genAi
PATH = os.path.join(BASE_DIR, "..", "..", "notes", "langchain_note.pdf")

# Normalize the path (removes ".." parts)
PATH = os.path.abspath(PATH)

print("PATH:", PATH)

loader = PyPDFLoader(PATH)

docs = loader.load()

print(len(docs))
print(docs[0].page_content)
print(docs[1].metadata)
