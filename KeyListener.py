import pyperclip
import time
from pynput import keyboard
from mpi4py import MPI
from utills import (
    copy_selected_text_to_clipboard,
    get_active_app_name,
    get_active_url,
    extract_website_name,
)


class KeyListener:
    def __init__(self, comm: MPI.Comm, writer: int):
        self.comm = comm
        self.writer = writer
        self.current_keys = set()
        self.COMBINATION = {
            keyboard.Key.cmd,
            keyboard.Key.ctrl,
            keyboard.KeyCode.from_char("r"),
        }
        self.listener = keyboard.Listener(
            on_press=self.on_key_down, on_release=self.on_key_up
        )
        self.is_activated = False  # Flag to track activation

    def on_key_down(self, key):
        if key in self.COMBINATION:
            self.current_keys.add(key)
            if all(k in self.current_keys for k in self.COMBINATION):
                if not self.is_activated:
                    self.is_activated = True
                    self.on_activate()
                    time.sleep(2)

    def on_key_up(self, key):
        if key in self.COMBINATION:
            # check if key is in the set
            if key in self.current_keys:
                self.current_keys.remove(key)
        self.is_activated = False  # Reset the flag when any key is released

    def on_activate(self):
        time.sleep(0.1)
        copy_selected_text_to_clipboard()
        # get the application where the text is copied from
        app = get_active_app_name()
        if app == "Google Chrome" or app == "Safari" or app == "firefox":
            url = get_active_url()
            app = extract_website_name(url)
        sentence = pyperclip.paste()
        # send the data to the master process
        data = [sentence, app]
        self.comm.send(data, dest=self.writer)

    def start(self):
        with self.listener as listener:
            listener.join()
