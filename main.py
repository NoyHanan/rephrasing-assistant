import os
import tkinter as tk
from models import GooglePaLM
from utills import rephrase, INITIAL_MESSAGE

# Set up the bot
api_key = os.environ["PALM_API_KEY"]
bot = GooglePaLM(api_key)

root = tk.Tk()
root.geometry("600x500")
root.title("Rephrase Assistant")

# Create the output box with a monospace font
terminal_output = tk.Text(root, wrap=tk.WORD, height=30, width=70, font="monospace", spacing1=2)
terminal_output.pack(padx=10, pady=10)

root.bind("<Command-p>", lambda event: rephrase(bot, terminal_output))
terminal_output.insert(tk.END, f"{INITIAL_MESSAGE}\n")

root.mainloop()
