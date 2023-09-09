from config import PROMPT_TEMPLATE, MODELS
from mpi4py import MPI


# message to be displayed on the terminal
INITIAL_MESSAGE = (
    "Assistant: I am your {model_str} rephrasing expert! provide me with "
    "a sentence and I will rephrase it according to the application."
)


def run_app(model_str: str, api_key: str, comm: MPI.Comm, sender: int) -> None:
    print(f"{INITIAL_MESSAGE.format(model_str=model_str)}", flush=True)
    print("-" * 79)
    llm = MODELS[model_str](api_key)
    while True:
        sentence, app = comm.recv(source=sender)
        # change the {app} and {sentence} in the prompt template to the actual
        # values of the app and sentence
        print("rephrasing.....", flush=True)
        print(f"app: {app}", flush=True)
        print(f"original sentence: {sentence}", flush=True)
        sentence = PROMPT_TEMPLATE.format(app=app, sentence=sentence)
        rephrased_sentence = llm(sentence)
        print(f"\nAssistant: {rephrased_sentence}", flush=True)
        print("-" * 79)
