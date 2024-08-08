import openai
import streamlit as st
from openai import OpenAI
from openai import AssistantEventHandler

client = OpenAI(api_key="")

thread = client.beta.threads.create()

# Set the assistant ID and initialize the OpenAI client with your API key
assistant_id = ""

st.title("💬 Regulatory Analyst Chatbot")
st.caption("🚀 A streamlit chatbot with information on regulatory dataset, entities, and risk categories")

prompt = st.text_input("Enter your message")
if prompt:
    with client.beta.threads.runs.stream(
            thread_id=thread.id,
            assistant_id=assistant_id,
            model="gpt-4o",
    ) as stream:
        with st.chat_message("assistant"):
            response = st.write_stream(stream.text_deltas)
            stream.until_done()


