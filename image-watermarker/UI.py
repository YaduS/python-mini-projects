from tkinter import *
from tkinter import ttk


class UI:

    def __init__(self) -> None:
        self.root = Tk()
        self.config_main_ui()

    def config_main_ui(self):
        self.root.title("Image Water marker")
        root = self.root

        root.configure(width=200, height=200)
        mainframe = ttk.Frame(root, padding="3 3 12 12", width=200, height=200)
        mainframe.grid(column=0, row=0)
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        root.configure()

        ttk.Button(mainframe, text="Open Image", command=self.load_image).grid(
            column=1, row=1
        )
        ttk.Label(mainframe, text="feet").grid(column=1, row=2)

        watermark_text = StringVar()
        watermark_entry = ttk.Entry(mainframe, width=7, textvariable=watermark_text)
        watermark_entry.grid(column=1, row=3)

        ttk.Button(
            mainframe, text="Open Image", command=self.save_watermark_image
        ).grid(column=1, row=4)

        for child in mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)

        self.watermark_text = watermark_text
        self.mainframe = mainframe

        root.mainloop()

    def load_image(self):

        # open file selector here
        pass

    def set_watermark_text(self):
        pass

    def set_watermark_position(self):
        pass

    def save_watermark_image(self):
        pass
