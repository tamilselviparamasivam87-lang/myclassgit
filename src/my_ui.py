
import streamlit as st
import requests

# Page configuration
st.set_page_config(
    page_title="My AI Chatbot",
    page_icon="🤖",
    layout="centered"
)

# API endpoint
API_URL = "http://127.0.0.1:8000/my-chatbot"

# Custom CSS
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #101827, #1e293b);
    color: white;
}

.main-title {
    text-align: center;
    font-size: 38px;
    font-weight: bold;
    color: #8BBAFF;
    padding: 10px;
}

.subtitle {
    text-align: center;
    color: #CBD5E1;
    font-size: 16px;
    margin-bottom: 30px;
}

.stChatMessage {
    border-radius: 15px;
    padding: 12px;
}

[data-testid="stChatInput"] {
    border-radius: 15px;
}

</style>
""", unsafe_allow_html=True)


# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []


# Sidebar
with st.sidebar:
    st.title("🤖 My AI Assistant")

    st.write("Welcome to your personal AI chatbot!")

    st.divider()

    if st.button("🗑️ Clear Chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

    st.divider()

    st.caption("Powered by")
    st.markdown("⚡ Groq LLM")
    st.markdown("🚀 FastAPI")
    st.markdown("🎨 Streamlit")


# Main heading
st.markdown(
    '<div class="main-title">✨ My AI Chatbot</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Ask anything. Your AI assistant is ready to help!</div>',
    unsafe_allow_html=True
)


# Welcome message
if not st.session_state.messages:
    st.info("👋 Hello! Welcome. Start a conversation below.")


# Display previous messages
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# Chat input
if prompt := st.chat_input("💬 Type your message here..."):

    # Display user message
    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    with st.chat_message("user"):
        st.markdown(prompt)

    # Get AI response
    with st.chat_message("assistant"):

        with st.spinner("🤖 AI is thinking..."):

            try:
                response = requests.post(
                    API_URL,
                    json={"message": prompt},
                    timeout=60
                )

                response.raise_for_status()

                result = response.json()

                ai_response = result["response"]

            except requests.exceptions.ConnectionError:
                ai_response = (
                    "❌ Cannot connect to FastAPI. "
                    "Please start your backend server."
                )

            except requests.exceptions.Timeout:
                ai_response = "⏳ Request timed out. Please try again."

            except requests.exceptions.RequestException as e:
                ai_response = f"❌ API Error: {e}"

            except (ValueError, KeyError):
                ai_response = "❌ Invalid response received from the API."

        st.markdown(ai_response)

    # Save assistant response
    st.session_state.messages.append({
        "role": "assistant",
        "content": ai_response
    })
