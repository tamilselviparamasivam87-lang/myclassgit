import os
from openai import OpenAI

from dotenv import load_dotenv


load_dotenv()

key = os.getenv("GROQ_API_KEY")

client = OpenAI(
    api_key = key,
    base_url="https://api.groq.com/openai/v1"
)

history=[]

def chatbot(user_input):

    print(history)

    history.append({
        "role" : "user", 
        "content" : user_input 

    })

 
    response = client.responses.create(
       model="openai/gpt-oss-120b",
       input=history

   )
    
    res = response.output_text

    history.append({
       "role": "assistant",
        "content" :res
    })



    return res
