import os
from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PATH = os.path.join(BASE_DIR, "books")
loader = DirectoryLoader(
    path=PATH,
    glob='*.pdf',
    loader_cls=PyPDFLoader
)

docs = loader.lazy_load()

for document in docs:
    print(document.metadata)