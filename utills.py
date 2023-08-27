import tkinter as tk
from KeyListener import KeyListener
from models import LLM
from tkinter import scrolledtext
from models import GooglePaLM
from config import INITIAL_MESSAGE
from multiprocessing import Queue


constructors = {"GooglePaLM": GooglePaLM}


def rephrase(message: str, output: tk.Text) -> None:
    output.configure(state="normal")
    output.insert(tk.END, "-" * (output["width"] - 1) + "\n")
    output.insert(tk.END, "Rephrasing...\n")
    # output.insert(tk.END, f"User: {message}\n")
    output.insert(tk.END, f"Assistant: {message}\n")
    output.configure(state="disabled")


def check_queue(root, queue, terminal_output):
    try:
        message = queue.get_nowait()
        rephrase(message, terminal_output)
    except:  # Queue is empty
        pass
    root.after(100, check_queue, root, queue, terminal_output)  # Check every 100ms


def run_app(queue: Queue) -> None:
    # llm = GooglePaLM(PALM_API_KEY)
    root = tk.Tk()
    root.geometry("600x500")
    root.title("Rephrase Assistant")

    terminal_output = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=("Courier", 14))
    terminal_output.pack(padx=10, pady=10, expand=True, fill=tk.BOTH)

    # root.bind("<Command-p>", lambda event: rephrase(llm, terminal_output))
    terminal_output.configure(state="normal")
    terminal_output.insert(tk.END, f"{INITIAL_MESSAGE}\n")
    terminal_output.configure(state="disabled")

    check_queue(root, queue, terminal_output)  # Start the periodic check
    root.mainloop()


def run_listener(model_str: str, api_key: str, queue: Queue) -> None:
    llm = constructors[model_str](api_key)
    key_listener = KeyListener(llm, queue)
    key_listener.start()
