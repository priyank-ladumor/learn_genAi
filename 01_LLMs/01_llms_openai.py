from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

# llm = ChatOpenAI(model="gpt-4") 
# response = llm.invoke(input="give me random a single boy name", temperature=0.7)
# print('result: ', response)

# llm = ChatOpenAI(model="gpt-5", instructions="Talk like a pirate.") 
# response = llm.invoke(input="what is 2+2")
# print('result: ', response)

llm = OpenAI(model='gpt-3.5-turbo-instruct')
result = llm.invoke("What is the capital of India")

print(result)