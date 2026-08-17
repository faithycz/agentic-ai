from dotenv import load_dotenv
from openai import OpenAI
import os

def setup():
    load_dotenv("../.env", override=True)

    openai_api_key = os.getenv("OPENAI_API_KEY")

    if openai_api_key:
        print(f"OpenAI API Key exists and begins {openai_api_key[:8]}")
    else:
        print("OpenAI API Key not set - please head to the troubleshooting guide in the setup folder")

def prompt_llm(model: str, question: str, client: OpenAI) -> str | None:
    messages = [{"role": "user", "content": question}]
    response = client.chat.completions.create(model=model, messages=messages)
    response_text = response.choices[0].message.content
    return response_text