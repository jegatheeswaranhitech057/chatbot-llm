import streamlit as st
import ollama

st.title("🤖 Local AI Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous chats
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# User input
prompt = st.chat_input("Ask something...")

if prompt:
   
    st.session_state.messages.append(
        {"role":"user","content":prompt}
    )

    with st.chat_message("user"):
        st.write(prompt)

    response = ollama.chat(
        model="llama3.2:latest",
        messages=st.session_state.messages
    )

    answer = response["message"]["content"]

    st.session_state.messages.append(
        {"role":"assistant","content":answer}
    )

    with st.chat_message("assistant"):
        st.write(answer)