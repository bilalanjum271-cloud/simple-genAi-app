import os 
from dotenv import load_dotenv
load_dotenv()
### for langchain tracking
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_PROJECT"]=os.getenv("LANGCHAIN_PROJECT", "default-project")

### for user/ web interface  interface 
import streamlit as st
from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
prompt=ChatPromptTemplate.from_messages(
    [
    ("system", "You are a helpful assistant"),
    ("human", "question: {question}")
])
#### for streamlit frameworks
st.title("simple genAi App using ollama")
input_text=st.text_input("what type of quetion you have in mind?")

### for ollama model
llm=Ollama(model="llama3")
output=StrOutputParser()
chain=prompt|llm|output

if input_text:
    st.write(chain.invoke({"question": input_text}))