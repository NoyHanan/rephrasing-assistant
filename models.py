import google.generativeai as palm
from google.generativeai.types import MessageOptions, ExampleOptions

CONTEXT = "You are a rephrasing expert."
INITIAL_MESSAGE = "I will give you a sentence and a specific context in which it will be used. Your task is to" \
                  " succinctly rephrase the sentence according to that context. Please keep your response brief," \
                  " unless otherwise instructed, and include only the restructured sentence. Now, in one sentence," \
                  " introduce yourself as my specialist in sentence rephrasing."
EXAMPLES = ("application: discord. message: Hi guys, I could really use your help with this issue, is anyone up?",
            "Hey everyone, I could really use some help with this issue. Is anyone available?")
class GooglePaLM:
    def __init__(self, api_key: str) -> None:
        palm.configure(api_key=api_key)
        self.chat = palm.chat(context=CONTEXT, messages=INITIAL_MESSAGE, temperature=0.0, candidate_count=1,
                              examples=EXAMPLES)

    def __call__(self, message: str) -> str:
        self.chat = self.chat.reply(message)
        return self.chat.last
