import os
from models import GooglePaLM

# MPI parameters
MASTER_RANK = 0
SUB_RANK = 1

PROMPT_TEMPLATE = "application: {app}. sentence: '{sentence}'"

# API keys
API_KEYS = {"GooglePaLM": os.environ["PALM_API_KEY"]}
MODELS = {"GooglePaLM": GooglePaLM}
