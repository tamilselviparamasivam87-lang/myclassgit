from openai import OpenAI

client = OpenAI()
#api_key="your api key"
response=client.responses.create(
    model="gpt-5.4-mini",
    input="actor ajith kumar"
    instructions="write a short paragraph",
    temperature=0,
    max_output_token=1000


    
)
print(response.output_text)
