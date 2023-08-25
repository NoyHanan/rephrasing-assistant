import tkinter as tk
import pyperclip
from models import Model

INITIAL_MESSAGE = "Assistant: I am your rephrasing expert! provide me with a sentence and an application and" \
                  " I will rephrase it according to the application."

def rephrase(model: Model, output: tk.Text) -> None:
    output.insert(tk.END, "--------------------------------------------------------------\n")
    clipboard_text = pyperclip.paste()
    output.insert(tk.END, f"User: {clipboard_text}\n")
    output.insert(tk.END, f"Assistant: {model(clipboard_text)}\n")
