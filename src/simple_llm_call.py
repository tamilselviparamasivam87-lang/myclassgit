import os
from openai import OpenAI


client = OpenAI(
    api_key=os.environ["OPENAI_API_KEY"]
)


response=client.responses.create(
    model="gpt-5.4-mini",
    input="actor ajith kumaar"

)
print(response.output_text)
