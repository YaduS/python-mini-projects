from tkinter import *
from tkinter import ttk, messagebox
import json
import random


class UI:

    def __init__(self):

        self.root = Tk()
        self.mainframe = None
        self.sample_text = None
        self.typed_text = None
        self.typing_area = None
        self.selected_words = None
        self.configure_ui()

    def configure_ui(self):

        self.root.title("Typing speed test")
        root = self.root
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        mainframe = ttk.Frame(root, padding="50 50 60 60")
        mainframe.grid(column=0, row=0)

        sample_text = StringVar()
        sample_text.set("sample text here")
        sample_text_label = Label(
            mainframe,
            textvariable=sample_text,
            borderwidth=2,
            relief="sunken",
            width=60,
            height=15,
            wraplength=340,
        )
        sample_text_label.grid(column=0, row=0, columnspan=2, sticky="ew")

        # typing area
        typed_text = StringVar()
        typing_area = ttk.Entry()
        typing_area = ttk.Entry(mainframe, width=60, textvariable=typed_text)
        typing_area.grid(column=0, row=1, pady=10)
        typing_area.bind("<Return>", self.handle_enter_clicked)

        # assign to globals
        self.mainframe = mainframe
        self.typed_text = typed_text
        self.sample_text = sample_text

    def launch_ui(self):
        self.load_words()
        self.root.mainloop()

    def listen_keystroke(self):
        pass

    def handle_enter_clicked(self, event):
        text: str = self.typed_text.get()
        text = text.replace("  ", " ")
        split_text = text.split(" ")
        print(split_text)
        score = 0
        for i, word in enumerate(self.selected_words):
            if i > len(split_text) - 1:
                break
            if word == split_text[i]:
                score += 1

        messagebox.showinfo("Score", f"your corrected WPM is {score}")

    def load_words(self):
        with open("./typing-speed-test/common-words.json") as file:
            all_words = json.load(file)
            selected_words = random.choices(all_words, k=100)
            paragraph = " ".join(selected_words)
            self.sample_text.set(paragraph)
            self.selected_words = selected_words
