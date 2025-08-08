
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()
# print(os.environ['OPENAI_API_KEY'])

model = ChatOpenAI(model='gpt-4', temperature=1.5, max_completion_tokens=6)
prompt = "Write a 3 line poem on cricket"
# result = model.invoke("Write a 3 line poem on cricket")
result = model.invoke(
    input=[
        {
            "role": "user", 
            "content": prompt
        }
    ]
)
print(result.content)


''' notes '''

''' temperature ''' 
# temperature used to control the randomness/creativity of the output

''' prompt ''' 
# The prompt parameter is the input text that the model uses to generate a response.

''' max_completion_tokens ''' 
# The max_completion_tokens parameter specifies the maximum number of tokens to generate in the response.

''' https://platform.openai.com/docs/models '''