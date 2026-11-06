# import os

# from openai import APIStatusError, OpenAI




# api_key = os.getenv("GROQ_API_KEY")
# if not api_key:
#     raise RuntimeError("Set the GROQ_API_KEY environment variable with a Groq API key.")

# client = OpenAI(api_key=api_key, base_url="https://api.groq.com/openai/v1")

# try:
#     response = client.chat.completions.create(
#         model="openai/gpt-oss-120b",
#         messages=[
#             {"role": "system", "content": "You are a helpful assistant."},
#             {
#                 "role": "user",
#                 "content": "Who is vijay.",
#             },
#         ],
#     )
# except APIStatusError as error:
#     print(f"Groq API error ({error.status_code}): {error.message}")
#     if error.body:
#         print(error.body)
#     raise

# print(response.choices[0].message.content)


from openai import OpenAI

client = OpenAI(
)  #openai api key from the env


response=client.responses.create(
    model="gpt-5.4-mini",
    input="actor ajith kumaar"

)
print(response.output_text)