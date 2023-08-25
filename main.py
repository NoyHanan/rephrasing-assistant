import google.generativeai as palm
import os
from models import GooglePaLM

print("Assistant: I am your rephrasing expert! provide me with a sentence and an application and I will "
      "rephrase it according to the application.")

# Set up the bot
api_key = os.environ["PALM_API_KEY"]
bot = GooglePaLM(api_key)

while True:
    message = input("User: ")
    print(f"Assistant: {bot(message)}")
