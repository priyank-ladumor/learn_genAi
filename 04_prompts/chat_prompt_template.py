from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

model = ChatOpenAI()
chat_template = ChatPromptTemplate([
    ('system', 'You are a helpful {domain} expert'),
    ('human', 'Explain in simple terms, what is {topic}')
])

prompt = chat_template.invoke({'domain':'cricket','topic':'best cricketer'})

# print(prompt)

result = model.invoke(prompt)

print(result.content)

''' ChatPromptTemplate:
# ChatPromptTemplate is a subclass of PromptTemplate that is specifically designed for chat models.
# It allows you to create a prompt template that can be used to generate chat messages. 
# It takes a list of tuples as input, where each tuple contains a role and a message.
# The role can be 'system', 'user', or 'assistant', and the message is the actual message content.
'''

''' MessagesPlaceholder: 
# MessagesPlaceholder is a special placeholder that can be used in a prompt template to represent a list of chat messages.
# It can be used in conjunction with ChatPromptTemplate to create a prompt template that can generate chat messages.
'''
