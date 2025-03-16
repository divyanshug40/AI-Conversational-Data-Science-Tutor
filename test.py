import streamlit as st
from transformers import pipeline
import torch

from huggingface_hub import login
from dotenv import load_dotenv
import os
h_token = os.getenv("hf_token")

login(token=h_token)

# Set up the Streamlit page
st.set_page_config(page_title="Chat with LLaMA", page_icon=":robot:", layout="wide")

# Title
st.title("Chat with LLaMA")

# Add a chat history container
if 'messages' not in st.session_state:
    st.session_state.messages = []

# Initialize the pipeline
pipe = pipeline("text-generation", model="meta-llama/Llama-2-7b-chat-hf", device=0 if torch.cuda.is_available() else -1)

# Function to display the chat
def display_chat():
    for message in st.session_state.messages:
        if message['role'] == 'user':
            st.markdown(f"**You:** {message['content']}")
        else:
            st.markdown(f"**LLaMA:** {message['content']}")

# Display previous conversation
display_chat()

# Input for user message
user_input = st.text_input("You:", "")

if user_input:
    # Add the user message to the chat history
    st.session_state.messages.append({'role': 'user', 'content': user_input})

    # Generate a response using the pipeline
    response = pipe(user_input, max_length=150, num_return_sequences=1)

    # Get the first generated response (if more sequences are generated, you can modify this part)
    generated_text = response[0]['generated_text']

    # Add the model's response to the chat history
    st.session_state.messages.append({'role': 'assistant', 'content': generated_text})

    # Redisplay the updated chat
    display_chat()

# Optional: Add a clear chat button
if st.button("Clear Chat"):
    st.session_state.messages = []
    st.experimental_rerun()
