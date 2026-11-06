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

while True:

    user_input=input("user : ")

    if user_input =="stop":
        print("stopping the chat")
        break

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


    print("AI :" + response.output_text)