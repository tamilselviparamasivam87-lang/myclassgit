
import streamlit as st
import requests

# --------------------------------
# PAGE CONFIGURATION
# --------------------------------

st.set_page_config(
    page_title="AI Chat Assistant",
    page_icon="🤖",
    layout="centered"
)

API_URL = "http://127.0.0.1:8000/my-chatbot"


# --------------------------------
# CUSTOM CSS
# --------------------------------

st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #101827, #172554);
    color: white;
}

.main-title {
    text-align: center;
    font-size: 38px;
    font-weight: 800;
    color: #60A5FA;
    margin-bottom: 5px;
}

.sub-title {
    text-align: center;
    color: #CBD5E1;
    font-size: 15px;
    margin-bottom: 30px;
}

.stChatMessage {
    background-color: #243449;
    border-radius: 15px;
    border: 1px solid #334155;
}

</style>
""", unsafe_allow_html=True)


# --------------------------------
# SESSION STATE
# --------------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

if "user_id" not in st.session_state:
    st.session_state.user_id = "user_001"


# --------------------------------
# SIDEBAR
# --------------------------------

with st.sidebar:

    st.title("🤖 AI Assistant")

    st.write("Your personal AI chatbot")

    st.divider()

    st.subheader("User Settings")

    entered_user_id = st.text_input(
        "Enter User ID",
        value=st.session_state.user_id
    )

    # Change user
    if entered_user_id != st.session_state.user_id:

        st.session_state.user_id = entered_user_id.strip()
        st.session_state.messages = []
        st.rerun()

    st.write("Current User:", st.session_state.user_id)

    st.divider()

    # Clear chat
    if st.button(
        "🗑️ Clear Conversation",
        use_container_width=True
    ):

        st.session_state.messages = []
        st.rerun()

    st.divider()

    st.markdown("### Technology")

    st.write("⚡ Groq LLM")
    st.write("🚀 FastAPI")
    st.write("🎨 Streamlit")

    st.divider()

    st.caption("AI Chat Assistant | Python Project")


# --------------------------------
# MAIN HEADER
# --------------------------------

st.markdown(
    '<div class="main-title">✨ My AI Chatbot</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="sub-title">Your intelligent AI assistant. Ask me anything!</div>',
    unsafe_allow_html=True
)


# --------------------------------
# WELCOME MESSAGE
# --------------------------------

if not st.session_state.messages:

    st.info(
        "👋 Welcome! Start a conversation with your AI assistant."
    )

    st.markdown("### 💡 Try asking")

    st.write("• What is Python?")
    st.write("• Explain Artificial Intelligence")
    st.write("• What is Machine Learning?")


# --------------------------------
# DISPLAY CHAT HISTORY
# --------------------------------

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])


# --------------------------------
# USER CHAT INPUT
# --------------------------------

if prompt := st.chat_input("💬 Type your message here..."):

    if not st.session_state.user_id:

        st.error("Please enter a valid User ID.")

    else:

        # Display user message
        st.session_state.messages.append({
            "role": "user",
            "content": prompt
        })

        with st.chat_message("user"):
            st.markdown(prompt)


        # --------------------------------
        # CALL FASTAPI BACKEND
        # --------------------------------

        with st.chat_message("assistant"):

            with st.spinner("🤖 AI is thinking..."):

                try:

                    response = requests.post(
                        API_URL,
                        json={
                            "message": prompt,
                            "user_id": st.session_state.user_id
                        },
                        timeout=90
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

                    ai_response = (
                        "⏳ Request timed out. Please try again."
                    )

                except requests.exceptions.HTTPError as e:

                    ai_response = f"❌ Backend HTTP error: {e}"

                except requests.exceptions.RequestException as e:

                    ai_response = f"❌ Request error: {e}"

                except (ValueError, KeyError):

                    ai_response = (
                        "❌ Invalid response received from backend."
                    )

            st.markdown(ai_response)


        # --------------------------------
        # SAVE AI RESPONSE
        # --------------------------------

        st.session_state.messages.append({
            "role": "assistant",
            "content": ai_response
        })

