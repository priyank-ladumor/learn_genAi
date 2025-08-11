from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate,load_prompt

load_dotenv()
model = ChatOpenAI()

st.header('Reasearch Tool')

paper_input = st.selectbox( "Select Research Paper Name", ["Attention Is All You Need", "BERT: Pre-training of Deep Bidirectional Transformers", "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis"] )

style_input = st.selectbox( "Select Explanation Style", ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"] ) 

length_input = st.selectbox( "Select Explanation Length", ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"] )

template = load_prompt('../template.json') 

# template = load_prompt('../04_prompts/template.json')

# template = PromptTemplate(
#      input_variables=["paper_input", "style_input", "length_input"],
#      template="""Please summarize the research paper titled "{paper_input}" with the following specifications:
# Explanation Style: {style_input} 
# Explanation Length: {length_input} 
# 1. Mathematical Details: 
#     - Include relevant mathematical equations if present in the paper. 
#     - Explain the mathematical concepts using simple, intuitive code snippets where applicable. 
# 2. Analogies: 
#     - Use relatable analogies to simplify complex ideas. 
# If certain information is not available in the paper, respond with: "Insufficient information available" instead of guessing. 
# Ensure the summary is clear, accurate, and aligned with the provided style and length.
# """,
# validate_template=True
# )


if st.button('Summarize'):
    chain = template | model
    result = chain.invoke({
        'paper_input':paper_input,
        'style_input':style_input,
        'length_input':length_input
    })
    
    st.write(result.content)
    
    
    
''' what is streamlit? 
Streamlit is a Python framework for quickly building interactive web apps, especially for data science, machine learning, and analytics projects.

You can think of it as a way to turn a Python script into a shareable web app without needing to know HTML, CSS, or JavaScript.
For example, you can:

 - Display charts, tables, and maps.

 - Add widgets like sliders, checkboxes, and dropdowns.

 - Show images, audio, or video.

 - Easily update the UI when variables change — no manual frontend coding.

# pip install streamlit
# streamlit run app.py
'''