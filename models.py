import google.generativeai as palm
import openai


class LLM:
    def __call__(self, message: str) -> str:
        raise NotImplementedError


class GooglePaLM(LLM):
    CONTEXT = "You job is to rephrase the sentences I'll give you according \
        to the context of the application"
    INITIAL_PROMPT = "I will give you a sentence and a specific context in \
        which it will be used. Your task is to succinctly rephrase the \
        sentence according to that context. Please keep your response brief, \
        unless otherwise instructed, and include only the restructured \
        sentence."
    EXAMPLES = [
        (
            "application: discord. sentence: 'Hi guys, I could really use \
            your help with this issue, is anyone up?'",
            "Hey everyone, I could really use some help with this issue. \
            Is anyone available?",
        )
    ]

    def __init__(self, api_key: str) -> None:
        palm.configure(api_key=api_key)
        self.chat = palm.chat(
            context=self.CONTEXT,
            messages=self.INITIAL_PROMPT,
            temperature=0.0,
            candidate_count=1,
            examples=self.EXAMPLES,
        )

    def __call__(self, message: str) -> str:
        self.chat = self.chat.reply(message)
        return self.chat.last


class OpenAI(LLM):
    MODEL = "gpt-3.5-turbo"
    CONTEXT = "As a model proficient in English rephrasing, your \
        objective is to modify the provided sentence to align with the \
        designated `talk style` of the application. In addition, you \
        should also mention the `talk style` you used. \
        Here's an illustration: \
        Given: \
        Application: Discord. Sentence: 'Hi guys, I could really use \
        your help with this issue, is anyone up?' \
        response: \
        Talk Style: 'Discord conversation' \
        Suggested Rephrase: 'Hey everyone, I need some \
        assistance. Is anyone online?'"

    def __init__(self, api_key: str) -> None:
        openai.api_key = api_key

    def __call__(self, message: str) -> str:
        response = openai.ChatCompletion().create(
            model=self.MODEL,
            messages=[
                {"role": "system", "content": self.CONTEXT},
                {"role": "user", "content": message},
            ],
        )
        return response["choices"][0]["message"]["content"]
