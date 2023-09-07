from models import GooglePaLM, OpenAI

# MPI parameters
MASTER_RANK = 0
SUB_RANK = 1

# prompt parameters
PROMPT_TEMPLATE = "application: {app}. sentence: '{sentence}'"

# models constructors
MODELS = {
    "GooglePaLM": GooglePaLM,
    "OpenAI": OpenAI,
}
