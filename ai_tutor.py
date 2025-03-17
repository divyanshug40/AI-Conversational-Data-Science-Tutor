import streamlit as st
import time
import json
import google.generativeai as genai
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.runnables import RunnableLambda,RunnablePassthrough


from langchain_core.prompts import ChatPromptTemplate , MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
#from langchain_community.chat_message_histories import SQLChatMessageHistory 
#from langchain_core.runnables.history import RunnableWithMessageHistory
import os
from dotenv import load_dotenv

def get_chat_history(username):
    try:
        with open(f"chat_history/{username}.json", "r") as hfile:
            return json.load(hfile)
    except (FileNotFoundError, json.JSONDecodeError):
        return []
    
def save_chat_history(username): 
    with open(f"chat_history/{username}.json", "w") as hfile:
        json.dump(st.session_state.chat_history, hfile, indent=4)


st.set_page_config(page_title="Data Science Tutor",page_icon=":bar_chart:",layout="centered")

if "login" not in st.session_state:
    st.session_state.login = False


if not st.session_state.login:
    st.title("🤖 Data Science Tutor")
    username=st.text_input(label="Enter your username")
    if st.button("Login"):
        if not username:
            st.error("Please enter a username.")
        else:
            st.session_state.name = username
            st.session_state.login = True
            
            st.session_state.chat_history = get_chat_history(username)
            if len(st.session_state.chat_history):
                st.success("Chat history loaded successfully.")
                time.sleep(1)
            else:
                st.success("New session started.")
                time.sleep(1)
            st.rerun()
    st.stop()
    
username = st.session_state.name
with st.sidebar:
    st.title("🤖 Data Science Tutor")
    st.write(f"Hello {username.title()}!! 🎉🎉🎉")
    st.write(""" Welcome to the Data Science AI Tutor 🤖
I’m here to help you with all things related to **Data Science** and **AI**. Whether you're a beginner or an expert, ask me anything about:
- Machine Learning
- Data Analysis
- AI Algorithms
- Data Visualization
- Python for Data Science
- And much more!

Feel free to type your questions and let’s explore the world of data science together! 🚀
""")



#st.title("🤖 Data Science Tutor")

if not get_chat_history(username):
    st.chat_message("assistant").write("Feel free to ask anything regarding **data science**!")
else:

    for chat in get_chat_history(username):
        with st.chat_message("user"):
            st.markdown(f"{chat['user']}")
        with st.chat_message("assistant"):
            st.markdown(f"{chat['ai']}")


load_dotenv()
api_key = os.getenv("google_token")

if not api_key:
    st.error("⚠️ **API KEY not found**❗❗❗ Please add your Google API key to the `.env` file.")
    st.stop()

# Initialize Google API and AI Model
#genai.configure(api_key=api_key)
chat_model = ChatGoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=api_key)

# Prompt Tempate
chat_prompt = ChatPromptTemplate(
        messages=[
            ("system","""You are a helpful AI tutor for data science. 
                - You are chatting with a user who is asking a question. 
                - Reply normally if user is making an introduction.
                - If the user asks a question,check if the following question is **strictly** related to data science.
                - If it is, reply with the answer in details using examples and explanations.
                - If it is not, reply with "I am unable to answer that question. Please ask something related to data science."

             
             """),
             MessagesPlaceholder(variable_name="history"),
             ("human", "{user_input}"),
        ],
)

output_parser = StrOutputParser()

runnable_get_history = RunnableLambda(get_chat_history)

chain = RunnablePassthrough.assign(history= runnable_get_history) | chat_prompt | chat_model | output_parser

# Chat Input
user_input = st.chat_input("Type your data science question...")

if user_input:
    with st.chat_message("user"):
        st.markdown(f"{user_input}")

    with st.chat_message("assistant"):
        with st.spinner("Thinking... 🤔"):
            try:
                response = chain.invoke({"user_input": user_input})
                st.markdown(f"{response}")
                st.session_state.chat_history.append({"user": user_input, "ai": response})
                save_chat_history(username)
                st.rerun()

            except Exception as e:
                st.error(f"⚠️ Error ❗❗❗: {e}")