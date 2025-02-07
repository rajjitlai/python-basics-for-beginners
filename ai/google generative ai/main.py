import google.generativeai as genai

from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("GOOGLE_GENAI_KEY")

genai.configure(api_key=api_key)


def own_ai(text):
    # GenerativeModel doesn't work on latest version of Python
    model = genai.GenerativeModel(model_name="gemini-2.0-flash-exp")
    response = model.generate_content(text)

    return response.text


while True:
    text = input("Enter your prompt (exit to quit): ")

    if text.lower() == "exit":
        print("Thank you...")
        break

    response = own_ai(text)
    print("Khamba AI: ", response)

