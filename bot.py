import streamlit as st
import openai
import os
# Access the secret key
openai.api_key = st.secrets["OPENAI_API_KEY"]
st.title("Simple AI Chatbot")
st.markdown("A simple chatbot powered by OpenAI's GPT model.")

# Sidebar for user instructions
st.sidebar.title("About")
st.sidebar.info("Enter your query below, and the chatbot will respond!")

# Store chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Input box for user query
user_input = st.text_input("You:", "", key="user_input")

if user_input:
    # Add user input to session state
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    # Get response from OpenAI API
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=st.session_state.messages
        )
        assistant_reply = response.choices[0].message["content"]
        
        # Add assistant reply to session state
        st.session_state.messages.append({"role": "assistant", "content": assistant_reply})
    except Exception as e:
        st.error(f"Error: {e}")

# Display chat history
for message in st.session_state.messages:
    if message["role"] == "user":
        st.markdown(f"**You:** {message['content']}")
    else:
        st.markdown(f"**ChatGPT:** {message['content']}")

st.button("Clear Chat", on_click=lambda: st.session_state.messages.clear())
