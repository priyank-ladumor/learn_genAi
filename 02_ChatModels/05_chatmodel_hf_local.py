import os
from dotenv import load_dotenv

# Load environment variables (e.g., HUGGINGFACEHUB_API_TOKEN from .env file)
load_dotenv()

# -------------------------------
# Example 1: Using LangChain HuggingFaceEndpoint
# -------------------------------
# This method uses HuggingFace's **Inference API** via LangChain.
# - Requires internet and a Hugging Face API token.
# - Requests are sent to Hugging Face's cloud servers.
# - Works even if the model is too large to run locally.
# - Supports LangChain features (streaming, caching, integration with tools/agents).
# -------------------------------
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

llm = HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.2",  # Cloud-hosted model
    task="text2text-generation"
)
model = ChatHuggingFace(llm=llm)
result = model.invoke("What is the capital of India?")
print(result.content)


# -------------------------------
# Example 2: Using LangChain HuggingFacePipeline
# -------------------------------
# This method runs the model **locally** using transformers pipelines.
# - Requires the model to be downloaded locally.
# - Runs on your CPU/GPU without needing an API key.
# - Useful for offline inference.
# - Performance depends on your local hardware.
# -------------------------------
from langchain_huggingface import HuggingFacePipeline, ChatHuggingFace

llm = HuggingFacePipeline.from_model_id(
    model_id="google/flan-t5-small", 
    task="text2text-generation",
    pipeline_kwargs={"max_new_tokens": 64, "temperature": 0.0},
)

model = ChatHuggingFace(llm=llm)
resp = model.invoke("What is the capital of India?")
print("->", resp.content)
