from fastapi import FastAPI

app =FastAPI()

@app.post("/my-chatbot")
def my_chat_bot():
    return {
        "message" : " my simple chatbot"
    }

    