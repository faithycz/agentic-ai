from dotenv import load_dotenv
from openai import OpenAI, Stream
import os

from openai.types.chat import ChatCompletionChunk
from openai.types.chat.chat_completion import ChatCompletion

def setup(api_key: str) -> None:
    load_dotenv("../.env", override=True)

    openai_api_key = os.getenv(api_key)

    if openai_api_key:
        print(f"OpenAI API Key exists and begins {openai_api_key[:8]}")
    else:
        print("OpenAI API Key not set - please head to the troubleshooting guide in the setup folder")

def prompt_llm(model: str, question: str, base_url = "", api_key = "") -> str | None:
    if base_url == "":
        client = OpenAI()
    else:
        api_key_value = os.getenv(api_key)
        client = OpenAI(base_url=base_url, api_key=api_key_value)

    messages = [{"role": "user", "content": question}]
    response = client.chat.completions.create(model=model, messages=messages)
    response_text = response.choices[0].message.content
    return response_text

def prompt_llm_raw(model: str, question: str, base_url = "", api_key = "") -> ChatCompletion  | Stream[ChatCompletionChunk]:
    if base_url == "":
        client = OpenAI()
    else:
        api_key_value = os.getenv(api_key)
        client = OpenAI(base_url=base_url, api_key=api_key_value)

    messages = [{"role": "user", "content": question}]
    response = client.chat.completions.create(model=model, messages=messages)
    print(type(response))
    return response