from openai import OpenAI
from utils import setup, prompt_llm

def main():
    setup()

    model_list = ["gpt-5.4-nano", "gpt-5.4-mini"]
    question_list = [
        "What is 1 + 1?",
        "What is the value of pi?"
    ]

    client = OpenAI()

    for model in model_list:
        for question in question_list:
            resp = prompt_llm(model, question, client)
            print(resp)

if __name__ == "__main__":
    main()