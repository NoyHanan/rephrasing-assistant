import pyperclip
import time
from pynput import keyboard
from models import LLM
from multiprocessing import Queue


def copy_selected_text_to_clipboard():
    # This will simulate CMD+C on macOS, copying the selected text
    # with keyboard.Controller() as controller:
    controller = keyboard.Controller()
    controller.press(keyboard.Key.cmd)
    controller.press('c')
    controller.release('c')
    controller.release(keyboard.Key.cmd)

class KeyListener:
    def __init__(self, llm: LLM, queue: Queue):
        self.llm = llm
        self.queue = queue
        self.current_keys = set()
        self.COMBINATION = {keyboard.Key.cmd, keyboard.Key.ctrl, keyboard.KeyCode.from_char('r')}
        self.listener = keyboard.Listener(on_press=self.on_key_down, on_release=self.on_key_up)

    def on_key_down(self, key):
        if key in self.COMBINATION:
            self.current_keys.add(key)
            if all(k in self.current_keys for k in self.COMBINATION):
                self.on_activate()

    def on_key_up(self, key):
        if key in self.COMBINATION:
            if key in self.current_keys:  # check if key is in the set
                self.current_keys.remove(key)

    def on_activate(self):
        time.sleep(0.1)
        copy_selected_text_to_clipboard()
        print(f"{pyperclip.paste()}")
        message = self.llm(pyperclip.paste())
        self.queue.put(message)

    def start(self):
        with self.listener as listener:
            listener.join()
