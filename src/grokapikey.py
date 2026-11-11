import os
from pathlib import Path

from openai import OpenAI

from dotenv import load_dotenv


load_dotenv(Path(__file__).resolve().with_name(".env"))

key = os.getenv("GROQ_API_KEY")

client = OpenAI(

    api_key = key,
    base_url="https://api.groq.com/openai/v1"
)

conversation = {}


def chatbot(user_input, user_id):

    if user_id not in conversation:
        conversation[user_id] = []

    history = conversation[user_id]

    history.append({
        "role": "user",
        "content": user_input,
    })

    response = client.responses.create(
        model="openai/gpt-oss-120b",
        input=history,
    )

    res = response.output_text

    history.append({
        "role": "assistant",
        "content": res,
    })


    print(conversation)


    

    return res
