from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()
# os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

#Langsmith
os.environ["LANGCHAIN_TRACING_V2"] = os.getenv("LANGCHAIN_TRACING_V2")
os.environ["LANGCHAIN_ENDPOINT"] = os.getenv("LANGCHAIN_ENDPOINT")
os.environ["LANGCHAIN_PROJECT"] = os.getenv("LANGCHAIN_PROJECT")
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

prompt = ChatPromptTemplate.from_messages(
    [
        ("system","You are a helpful assistant. Please respond to the user questions"),
        ("user","Question:{question}")
    ]
)

## streamlit framework

st.title("Langchain Demo with Ollama Llama 3.2:1b")
input_text = st.text_input("search the topic you want")

llm = Ollama(model="llama3.2:1b")
output_parser = StrOutputParser()
chain=prompt|llm|output_parser

if input_text:
    st.write("assistant:" + chain.invoke({'question':input_text}))