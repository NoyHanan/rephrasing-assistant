from config import PROMPT_TEMPLATE, MODELS, COLOR_AND_BOLD, COLOR_RESET
from mpi4py import MPI


# message to be displayed on the terminal
INITIAL_MESSAGE = (
    COLOR_AND_BOLD
    + "Assistant: "
    + COLOR_RESET
    + "I am your {model_str} rephrasing expert! provide me with "
    "a sentence and I will rephrase it according to the application."
)


def run_app_mac(
    model_str: str,
    api_key: str,
    comm: MPI.Comm,
    sender: int,
) -> None:
    print(f"{INITIAL_MESSAGE.format(model_str=model_str)}", flush=True)
    print(
        COLOR_AND_BOLD + "-" * 79 + COLOR_RESET,
        flush=True,
    )
    llm = MODELS[model_str](api_key)
    while True:
        sentence, app = comm.recv(source=sender)
        # change the {app} and {sentence} in the prompt template to the actual
        # values of the app and sentence
        print(
            COLOR_AND_BOLD + "rephrasing....." + COLOR_RESET,
            flush=True,
        )
        print(
            COLOR_AND_BOLD + "app:",
            COLOR_RESET + app,
            flush=True,
        )
        print(
            COLOR_AND_BOLD + "original sentence:",
            COLOR_RESET + sentence,
            flush=True,
        )
        sentence = PROMPT_TEMPLATE.format(app=app, sentence=sentence)
        rephrased_sentence = llm(sentence)
        print(
            COLOR_AND_BOLD + "Assistant:",
            COLOR_RESET + rephrased_sentence,
            flush=True,
        )
        print(
            COLOR_AND_BOLD + "-" * 79 + COLOR_RESET,
            flush=True,
        )
