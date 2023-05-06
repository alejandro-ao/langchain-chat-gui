# python 3.8 (3.8.16) or it doesn't work

from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)
from dotenv import load_dotenv
import os
import streamlit as st
from streamlit_chat import message

load_dotenv()

# Load the OpenAI API key from the environment variable
if os.getenv("OPENAI_API_KEY") is None or os.getenv("OPENAI_API_KEY") == "":
    print("OPENAI_API_KEY is not set")
    exit(1)
else:
    print("OPENAI_API_KEY is set")
    

chat = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")

st.header("Your own ChatGPT 🤖")

if 'messages' not in st.session_state:
    st.session_state['messages'] = [SystemMessage(content="You are a helpful assistant.")]

user_input = st.text_input("You:", key='input')

if user_input:
    st.session_state.messages.append(HumanMessage(content=user_input))
    response = chat(st.session_state.messages)
    st.session_state.messages.append(AIMessage(content=response.content))
    

messages = st.session_state.get('messages', [])
with st.spinner("Generating messages..."):
    for i, msg in enumerate(messages[1:]):
        if i % 2 == 0:
            message(msg.content, is_user=True, key=str(i) + '_user')
        else:
            message(msg.content, is_user=False, key=str(i) + '_ai')