from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGlE_API_KEY"))

##Funvtion to load gemini pro model and get response
model=genai.GenerativeModel("gemini-pro")
chat=model.start_chat(history=[])

def getgemini_response(question):
    response=chat.send_message(question,stream=True)#
    return response

##initialize our streamlit app
st.set_page_config(page_title="QA DEMO")

st.header("GEMINI LLM APPLICATION")

##initialize session state for chat history if it doesnt exist
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = [] 
input=st.text_input("Input:",key="input")
submit=st.button("Ask the Question")

if submit and input:
    response=getgemini_response(input)
    ## add user query and response to session chat history
    st.session_state['chat_history'].append(("you",input))#storing all the chat
    st.subheader("The response:")
    for chunk in response:
        st.write(chunk.text)
        st.session_state['chat_history'].append(("bot",chunk.text))
st.subheader("The chat History is")

for role,text in st.session_state['chat_history']:
    st.write(f"{role}:{text}")

