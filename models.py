import google.generativeai as palm

CONTEXT = "You are a rephrasing expert."
INITIAL_MESSAGE = "I will give you a sentence and a specific context in which it will be used. Your task is to" \
                  " succinctly rephrase the sentence according to that context. Please keep your response brief," \
                  " unless otherwise instructed, and include only the restructured sentence. Now, in one sentence," \
                  " introduce yourself as my specialist in sentence rephrasing."
EXAMPLES = [("user: application: discord. sentence: Hi guys, I could really use your help with this issue, is anyone up?",
            "assistant: Hey everyone, I could really use some help with this issue. Is anyone available?")]


class Model:
    def __call__(self, message: str) -> str:
        raise NotImplementedError

class GooglePaLM(Model):
    def __init__(self, api_key: str) -> None:
        palm.configure(api_key=api_key)
        self.chat = palm.chat(context=CONTEXT, messages=INITIAL_MESSAGE, temperature=0.0, candidate_count=1,
                              examples=EXAMPLES)

    def __call__(self, message: str) -> str:
        self.chat = self.chat.reply(message)
        return self.chat.last
