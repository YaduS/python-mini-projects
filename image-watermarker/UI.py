from tkinter import *
from tkinter import ttk
from tkinter import filedialog

from ImageProcessor import ImageProcessor


class UI:

    def __init__(self) -> None:
        self.root = Tk()

        # to be used later
        self.loaded_image = None
        self.loaded_image_label: Label = None
        self.watermark_text = None
        self.mainframe = None

        self.config_main_ui()

    def config_main_ui(self):
        self.root.title("Image Water marker")
        root = self.root

        mainframe = ttk.Frame(root, padding="100 100 120 120")
        mainframe.grid(column=0, row=0)
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        root.configure()

        ttk.Button(mainframe, text="Open Image", command=self.load_image).grid(
            column=1, row=1
        )
        self.loaded_image_label = ttk.Label(mainframe, text="Add an image file")

        self.loaded_image_label.grid(column=1, row=2)
        # hide the label till its ready to be displayed
        self.loaded_image_label.grid_remove()

        watermark_text = StringVar()
        watermark_entry = ttk.Entry(mainframe, width=7, textvariable=watermark_text)
        watermark_entry.grid(column=1, row=3)

        ttk.Button(
            mainframe, text="Save Image", command=self.save_watermark_image
        ).grid(column=1, row=4)

        for child in mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)

        self.watermark_text = watermark_text
        self.mainframe = mainframe

    def start_ui(self):
        self.root.mainloop()

    def load_image(self):

        # Opens the file selector dialog
        file_path = filedialog.askopenfilename(
            title="Select a file",
            filetypes=(
                ("Image files", "*.jpg *.png *.jpeg"),
                ("All files", "*.*"),
            ),
        )

        if file_path:
            print(f"File selected: {file_path}")
            self.loaded_image_label.configure(text=f"file: {file_path}")
            self.loaded_image_label.grid()
            self.loaded_image = ImageProcessor(file_path)
        else:
            print("No file selected")

    def save_watermark_image(self):
        self.loaded_image.watermark(self.watermark_text.get())
