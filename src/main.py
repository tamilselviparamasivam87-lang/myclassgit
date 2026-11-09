from fastapi import FastAPI
from pydantic import BaseModel

from src.grokapikey import chatbot

app =FastAPI()

class ChatbotRequest(BaseModel):
    message :str
class ChatbotResponse(BaseModel):
    response :str
    

@app.post("/my-chatbot")
def my_chat_bot(request:ChatbotRequest):

    response=chatbot(request.message)

    return ChatbotResponse(response=response)

    
    