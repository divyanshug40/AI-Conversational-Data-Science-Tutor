import streamlit as st
from transformers import AutoModelForCausalLM, AutoTokenizer 
import torch

from huggingface_hub import login
login(token="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")

# Load the LLaMA model and tokenizer from Hugging Face
model_name = "meta-llama/Llama-2-7b-chat-hf"  # You can change this to another LLaMA variant if needed

# Initialize the tokenizer and model
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Set up the Streamlit page
st.set_page_config(page_title="Chat with LLaMA", page_icon=":robot:", layout="wide")

# Title
st.title("Chat with LLaMA")

# Add a chat history container
if 'messages' not in st.session_state:
    st.session_state.messages = []

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

    # Tokenize the user input and generate a response from LLaMA
    inputs = tokenizer(user_input, return_tensors="pt")

    # Ensure that the model runs on the correct device (GPU if available)
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.to(device)
    inputs = {key: value.to(device) for key, value in inputs.items()}

    # Generate a response
    with torch.no_grad():
        output = model.generate(**inputs, max_length=150, num_return_sequences=1, no_repeat_ngram_size=2)

    # Decode the generated response
    response = tokenizer.decode(output[0], skip_special_tokens=True)

    # Add the model's response to the chat history
    st.session_state.messages.append({'role': 'assistant', 'content': response})

    # Redisplay the updated chat
    display_chat()

# Optional: Add a clear chat button
if st.button("Clear Chat"):
    st.session_state.messages = []
    st.experimental_rerun()
