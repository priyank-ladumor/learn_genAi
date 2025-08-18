from langchain_community.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.docstore.document import Document

emb = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2", encode_kwargs={"normalize_embeddings": True})

docs = [
    Document(page_content="Django is a Python web framework.", metadata={"id": 201, "topic": "python"}),
    Document(page_content="Next.js is a React framework.", metadata={"id": 202, "topic": "react"}),
    Document(page_content="FAISS does fast vector search.", metadata={"id": 203, "topic": "ml"}),
]

# CREATE
vs = FAISS.from_documents(docs, embedding=emb)

# READ (search)
res = vs.similarity_search_with_score("vector search library", k=2)
for d, sc in res:
    print(sc, d.page_content, d.metadata)

# ADD (more docs)
more = [Document(page_content="LangChain integrates with FAISS.", metadata={"id": 204})]
vs.add_documents(more)

# UPDATE (replace by custom IDs):
# LangChain's FAISS wrapper does not expose in-place update; do: delete then add.
# We'll keep our own IDs in metadata and a helper:

def delete_by_meta_id(vs: FAISS, meta_ids):
    # the FAISS wrapper stores an index_to_docstore_id map; we can rebuild keeping those we want
    keep_texts, keep_metas = [], []
    for doc in vs.docstore._dict.values():
        if doc.metadata.get("id") not in meta_ids:
            keep_texts.append(doc.page_content)
            keep_metas.append(doc.metadata)
    # rebuild vectorstore
    new_vs = FAISS.from_texts(keep_texts, embedding=emb, metadatas=keep_metas)
    return new_vs

# delete 202, then re-add as an "update"
vs = delete_by_meta_id(vs, [202])
vs.add_documents([Document(page_content="Next.js adds App Router and SSR.", metadata={"id": 202, "topic": "react"})])

# DELETE multiple
vs = delete_by_meta_id(vs, [201])

# SAVE / LOAD
vs.save_local("langchain_faiss_idx")
loaded = FAISS.load_local("langchain_faiss_idx", embeddings=emb, allow_dangerous_deserialization=True)
