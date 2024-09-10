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

        # declare attributes (for autocompletion and type hinting)
        self.image_name_label: ttk.Label = None
        self.image_preview_label: ttk.Label = None
        self.load_image_btn: ttk.Button = None
        self.filename: str = None

        self.config_main_ui()

    def config_main_ui(self):

        # root and mainframe
        self.root.title("Image Analyzer")
        root = self.root
        root.geometry("500x500")
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        mainframe = ttk.Frame(root, padding="50 50 60 60")
        mainframe.grid(column=0, row=0)
        self.mainframe = mainframe

        # Labels
        image_name_label = ttk.Label(mainframe, text="<Image Name>")
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

        # hide image preview and name label(until image is loaded)
        image_preview_label.grid_remove()
        image_name_label.grid_remove()

        # assign to attributes for later use
        self.image_name_label = image_name_label
        self.image_preview_label = image_preview_label
        self.load_image_btn = load_image_btn

    def start_ui(self):
        self.root.mainloop()

    def select_image(self):
        try:
            # Opens the file selector dialog
            file_path = filedialog.askopenfilename(
                title="Select a file",
                filetypes=(
                    ("Image files", "*.jpg *.png *.jpeg"),
                    ("All files", "*.*"),
                ),
            )
        except:
            print("closed file dialog box")
            return None

        filename_with_extension = os.path.basename(file_path)

        # assign to global for reuse
        self.filename = filename_with_extension

        return file_path

    def load_image(self):
        file_path = self.select_image()
        # if file unselected, return
        if not file_path:
            return

        self.img = Image.open(file_path)
        # attribute added to keep this in memory so that image can be displayed
        img_copy = self.img.copy()
        img_copy.thumbnail((IMAGE_MAX_WIDTH, IMAGE_MAX_HEIGHT))
        self.tk_converted_image = ImageTk.PhotoImage(img_copy)
        self.image_preview_label["image"] = self.tk_converted_image
        self.image_name_label.config(text=f"{self.filename}")

        self.image_preview_label.grid()
        self.image_name_label.grid()
