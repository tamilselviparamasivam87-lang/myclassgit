from openai import OpenAI

client = OpenAI()  #openai api key from the env


response=client.responses.create(
    model="gpt-5.4-mini",
    input="actor ajith kumaar"

)
print(response.output_text)
