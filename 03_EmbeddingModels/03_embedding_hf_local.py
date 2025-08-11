from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')

documents = [
    "Delhi is the capital of India",
    "Kolkata is the capital of West Bengal",
    "Paris is the capital of France"
]

query = "Delhi is the capital of India"
   

vector = embedding.embed_documents(documents)
vector_query = embedding.embed_query(query)

print(str(vector))
print('vector_query: ', str(vector_query))