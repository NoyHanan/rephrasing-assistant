from models import GooglePaLM, OpenAI
from colorama import Fore, Style

# MPI parameters
MASTER_RANK = 0
SUB_RANK = 1

# prompt parameters
PROMPT_TEMPLATE = "application: {app}. sentence: '{sentence}'"

# colorama parameters
COLOR_AND_BOLD = Fore.BLUE + Style.BRIGHT
COLOR_RESET = Style.RESET_ALL

# models constructors
MODELS = {
    "GooglePaLM": GooglePaLM,
    "OpenAI": OpenAI,
}
