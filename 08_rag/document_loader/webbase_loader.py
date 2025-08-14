from dotenv import load_dotenv

from langchain_community.document_loaders import WebBaseLoader
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

load_dotenv()

model = ChatOpenAI()

prompt = PromptTemplate(
    template='Answer the following question \n {question} from the following text - \n {text}',
    input_variables=['question','text']
)

parser = StrOutputParser()

url = 'https://www.amazon.in/Samsung-Galaxy-Smartphone-Storage-Offers/dp/B0DH76RM81/ref=sr_1_1?adgrpid=154581677239&dib=eyJ2IjoiMSJ9.hcXhdIGGxWAXzWF6VBL5JYWeipdKhLIcoDx6qUSM7d3FFcUzic1Xc_ljA0gLc4swTgDyOkbiuQ_ZMPE9WS5fgzRxeAtZMmhDNleAXN_j9OZ_MqIV1XuX0S4lvd6w6nN6Wd8k-MPBSHvXdtFyA91lT4QHQ9oIPwWkgTs1RuP3LwE4vzjXVPaIzPxuPCF4B0PejkQY_nGKafpiRufuVyJtyV-LboyXxRf_2MenT-HMxjk.ycU1D1PhFEIwkPLhcCUQaQLe-2oK4XMepCvw0MjoZhw&dib_tag=se&hvadid=679705697662&hvdev=c&hvlocphy=9062197&hvnetw=g&hvqmt=e&hvrand=2029815592263573973&hvtargid=kwd-1441260799674&hydadcr=24569_2265455&keywords=samsung+flip+6&mcid=4141550c3fbd30f5a6c691df2aa3064f&nsdOptOutParam=true&qid=1755173976&sr=8-1'
# url = 'https://www.flipkart.com/samsung-galaxy-z-flip6-5g-blue-256-gb/p/itm8f1b3aefb27f2'
loader = WebBaseLoader(url)

docs = loader.load()

print('docs[0].page_content: ', docs[0].page_content)

# chain = prompt | model | parser

# print(chain.invoke({'question':'What is the prodcut that we are talking about?', 'text':docs[0].page_content}))