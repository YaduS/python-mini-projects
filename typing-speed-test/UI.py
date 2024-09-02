from tkinter import *
from tkinter import ttk
import json
import random


class UI:

    def __init__(self):

        self.root = Tk()
        self.mainframe = None
        self.sample_text = None
        self.configure_ui()

    def configure_ui(self):

        self.root.title("Image Water marker")
        root = self.root
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        mainframe = ttk.Frame(root, padding="50 50 60 60")
        mainframe.grid(column=0, row=0)

        sample_text = StringVar()
        sample_text.set("sample text here")

        text_label = Label(
            mainframe,
            textvariable=sample_text,
            borderwidth=2,
            relief="sunken",
            width=60,
            height=15,
            wraplength=340,
        )
        text_label.grid(column=0, row=0, columnspan=2, sticky="ew")

        self.mainframe = mainframe
        self.sample_text = sample_text

    def launch_ui(self):
        self.load_words()
        self.root.mainloop()

    def listen_keystroke(self):
        pass

    def load_words(self):
        with open("./typing-speed-test/common-words.json") as file:
            all_words = json.load(file)
            selected_words = random.choices(all_words, k=100)
            paragraph = " ".join(selected_words)
            self.sample_text.set(paragraph)
