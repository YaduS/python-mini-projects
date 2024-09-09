import os
from tkinter import *
from tkinter import ttk, filedialog, messagebox
from PIL import ImageTk, Image


IMAGE_MAX_HEIGHT = 400
IMAGE_MAX_WIDTH = 400

TOTAL_GRID_COLUMNS = 1


class UI:

    def __init__(self) -> None:
        self.root = Tk()
        self.config_main_ui()

    def config_main_ui(self):

        # root and mainframe
        self.root.title("Image Analyzer")
        root = self.root
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        mainframe = ttk.Frame(root, padding="50 50 60 60")
        mainframe.grid(column=0, row=0)
        self.mainframe = mainframe

        # Labels
        image_name_label = ttk.Label(mainframe, text="Image Name: ")
        image_preview_label = ttk.Label(mainframe)
        image_name_label.grid(column=0, row=0)
        image_preview_label.grid(column=0, row=1)

        # Button
        load_image_btn = ttk.Button(
            mainframe,
            text="Load Image",
            command=self.load_image,
        )
        load_image_btn.grid(column=0, row=2)

        self.image_name_label = image_name_label
        self.image_preview_label = image_preview_label
        self.load_image_btn = load_image_btn

    def start_ui(self):
        self.root.mainloop()

    def select_image(self):
        # Opens the file selector dialog
        file_path = filedialog.askopenfilename(
            title="Select a file",
            filetypes=(
                ("Image files", "*.jpg *.png *.jpeg"),
                ("All files", "*.*"),
            ),
        )

        filename_with_extension = os.path.basename(file_path)
        name_without_extension = os.path.splitext(filename_with_extension)[0]
        self.filename = name_without_extension

        return file_path

    def load_image(self):
        file_path = self.select_image()

        self.img = Image.open(file_path)
        # attribute added to keep this in memory so that image can be displayed
        img_copy = self.img.copy()
        img_copy.thumbnail((IMAGE_MAX_WIDTH, IMAGE_MAX_HEIGHT))
        self.tk_converted_image = ImageTk.PhotoImage(img_copy)
        self.image_preview_label["image"] = self.tk_converted_image
