from tkinter import *
from tkinter import ttk, messagebox
import json
import random

TIME_LIMIT = 60  # 60 seconds


class UI:

    def __init__(self):

        self.root = Tk()
        self.mainframe = None
        self.sample_text = None
        self.typed_text_saved = []
        self.typed_text = None
        self.typing_area = None
        self.selected_words = None
        self.timer_text = None
        self.timer_label = None
        self.time_remaining = TIME_LIMIT
        self.timer_started = False
        self.configure_ui()

    def configure_ui(self):

        self.root.title("Typing speed test")
        root = self.root
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        mainframe = ttk.Frame(root, padding="50 50 60 60")
        mainframe.grid(column=0, row=0)

        # label for timer

        timer_text = StringVar()
        timer_text.set("Start typing to start timer: (60 seconds)")
        timer_label = Label(mainframe, textvariable=timer_text)
        timer_label.grid(column=0, row=0, sticky="ew")

        # sample text to be typed in
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
        sample_text_label.grid(column=0, row=1, columnspan=2, sticky="ew")

        # typing area
        typed_text = StringVar()
        typing_area = ttk.Entry()
        typing_area = ttk.Entry(
            mainframe, width=60, textvariable=typed_text, justify="center"
        )
        typing_area.grid(column=0, row=2, pady=10)
        typing_area.bind("<Key>", self.listen_keystroke)

        # assign to globals
        self.mainframe = mainframe
        self.typed_text = typed_text
        self.sample_text = sample_text
        self.typing_area = typing_area
        self.timer_text = timer_text
        self.timer_label = timer_label

    def launch_ui(self):
        self.load_words()
        self.root.mainloop()

    def listen_keystroke(self, event):
        # print(f"pressed key: {event.keysym} {event.keysym == "space"}")
        if event.keysym == "space":
            trimmed_text = self.typed_text.get().replace(" ", "")
            self.typed_text_saved.append(trimmed_text)
            self.typed_text.set("")
        if not self.timer_started:
            self.start_timer()
            self.timer_started = True

    def start_timer(self):
        self.root.after(1000, self.update_timer)
        self.timer_text.set(f"Time remaining: {self.time_remaining}")

    def update_timer(self):
        self.time_remaining -= 1
        self.timer_text.set(f"Time remaining: {self.time_remaining}")
        if self.time_remaining <= 0:
            self.finish_game()
        else:
            self.root.after(1000, self.update_timer)

    def finish_game(self):
        split_text = self.typed_text_saved
        # print(split_text)
        score = 0
        for i, word in enumerate(self.selected_words):
            if i > len(split_text) - 1:
                break
            if word == split_text[i]:
                score += 1

        messagebox.showinfo("Score", f"your corrected WPM is {score}")

        # can add code here to rest the timer and fetch new sets of words

    def load_words(self):
        with open("./typing-speed-test/common-words.json") as file:
            all_words = json.load(file)
            selected_words = random.choices(all_words, k=100)
            paragraph = " ".join(selected_words)
            self.sample_text.set(paragraph)
            self.selected_words = selected_words
