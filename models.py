import google.generativeai as palm
from config import CONTEXT, INITIAL_PROMPT, EXAMPLES

class LLM:
    def __call__(self, message: str) -> str:
        raise NotImplementedError

class GooglePaLM(LLM):
    def __init__(self, api_key: str) -> None:
        palm.configure(api_key=api_key)
        self.chat = palm.chat(context=CONTEXT, messages=INITIAL_PROMPT, temperature=0.0, candidate_count=1,
                              examples=EXAMPLES)

    def __call__(self, message: str) -> str:
        self.chat = self.chat.reply(message)
        return self.chat.last
