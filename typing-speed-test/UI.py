from tkinter import *
from tkinter import ttk


class UI:

    def __init__(self):

        self.root = Tk()
        self.mainframe = None
        self.configure_ui()

    def configure_ui(self):

        self.root.title("Image Water marker")
        root = self.root
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        mainframe = ttk.Frame(root, padding="50 50 60 60")
        mainframe.grid(column=0, row=0)

        text_label = Label(
            mainframe,
            text="sample text here",
            borderwidth=2,
            relief="sunken",
            width=30,
            height=5,
        )
        text_label.grid(column=0, row=0, columnspan=2, sticky="ew")

        self.mainframe = mainframe

    def launch_ui(self):
        self.root.mainloop()

    def listen_keystroke(self):
        pass

    def load_words(self):
        pass
