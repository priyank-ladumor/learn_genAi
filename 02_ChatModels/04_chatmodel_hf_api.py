from dotenv import load_dotenv
import os

load_dotenv()

''' Example 1: Chat with a Hugging Face model using the Hugging Face API directly '''

from huggingface_hub import InferenceClient

client = InferenceClient(token=os.getenv("HUGGINGFACEHUB_ACCESS_TOKEN"))

resp = client.chat.completions.create(
    model="mistralai/Mistral-7B-Instruct-v0.2",
    messages=[{"role": "user", "content": "What is the capital of India?"}],
    max_tokens=80
)
print("1 ->", resp.choices[0].message.content)


''' Example 2: Chat with a Hugging Face model using the LangChain wrapper '''

from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace

api_token = os.getenv("HUGGINGFACEHUB_ACCESS_TOKEN")
if not api_token:
    raise RuntimeError("HUGGINGFACEHUB_ACCESS_TOKEN not set in env")

llm = HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.2",  
    task="text-generation",
    temperature=0.5,     
    max_new_tokens=50,      
    huggingfacehub_api_token=api_token 
)

model = ChatHuggingFace(llm=llm)

resp = model.invoke("i have one cup of coffee and one cup of tea what is the difference between them?")
print("2 ->", resp.content)



""" Disadvantages of using the Hugging Face API directly:
- No built-in streaming support for most endpoints (you get the response only after it’s fully generated).
- No automatic caching of responses (every request hits the API, even if it's the same input).
- No direct integration with LangChain features (like memory, retrievers, or tool calling).
"""

""" Advantages of using the LangChain HuggingFace wrapper:
- Adds streaming support for compatible models.
- Supports LangChain's built-in caching mechanisms (local or external cache backends).
- Seamlessly integrates with LangChain tools, agents, and chains.
"""

