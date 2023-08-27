import os

# LLM parameters
CONTEXT = "You are a rephrasing expert."
INITIAL_PROMPT = "I will give you a sentence and a specific context in which it will be used. Your task is to" \
                  " succinctly rephrase the sentence according to that context. Please keep your response brief," \
                  " unless otherwise instructed, and include only the restructured sentence. Now, in one sentence," \
                  " introduce yourself as my specialist in sentence rephrasing."
EXAMPLES = [("application: discord. sentence: 'Hi guys, I could really use your help with this issue, is anyone up?'",
            "Hey everyone, I could really use some help with this issue. Is anyone available?")]

# message to be displayed on the terminal
INITIAL_MESSAGE = "Assistant: I am your rephrasing expert! provide me with a sentence and an application and" \
                  " I will rephrase it according to the application."

# API keys
API_KEYS = {"GooglePaLM": os.environ["PALM_API_KEY"]}