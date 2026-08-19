# if you dont use pipenv uncomment the following:
# from dotenv import load_dotenv
# load_dotenv()


#Step1: Setup UI with streamlit (model provider, model, system prompt, web_search, query)
import os

import streamlit as st

st.set_page_config(page_title="LangGraph Agent UI", layout="centered")
st.title("AI Chatbot Agents")
st.write("Create and Interact with the AI Agents!")

system_prompt=st.text_area("Define your AI Agent: ", height=70, placeholder="Type your system prompt here...")

MODEL_NAMES_GROQ = ["openai/gpt-oss-120b", "groq/compound-mini"]

provider="Groq"
st.info("Using Groq's free developer tier")
selected_model = st.selectbox("Select Groq Model:", MODEL_NAMES_GROQ)

allow_web_search=st.checkbox("Allow Web Search")

user_query=st.text_area("Enter your query: ", height=150, placeholder="Ask Anything!")

API_URL = os.getenv("BACKEND_URL", "http://127.0.0.1:9999") + "/chat"

if st.button("Ask Agent!"):
    if user_query.strip():
        #Step2: Connect with backend via URL
        import requests

        payload={
            "model_name": selected_model,
            "model_provider": provider,
            "system_prompt": system_prompt,
            "messages": [user_query],
            "allow_search": allow_web_search
        }

        try:
            response = requests.post(API_URL, json=payload, timeout=90)
            if response.ok:
                response_data = response.json()
                if isinstance(response_data, dict) and "error" in response_data:
                    st.error(response_data["error"])
                else:
                    st.subheader("Agent Response")
                    st.write(response_data)
            else:
                st.error(f"Backend error ({response.status_code}): {response.text}")
        except requests.RequestException as exc:
            st.error(f"Could not connect to the backend: {exc}")



