from tkinter import *
from tkinter import ttk, filedialog, messagebox
from PIL import ImageTk

from ImageProcessor import ImageProcessor

MAX_HEIGHT = 400
MAX_WIDTH = 400


class UI:

    def __init__(self) -> None:
        self.root = Tk()

        # to be used later
        self.watermark_text = None
        self.mainframe = None
        self.loaded_image = None
        self.loaded_image_path_label: Label = None
        self.loaded_image_preview_label: Label = None
        self.tk_converted_image = None
        self.watermarked_image_preview_label: Label = None
        self.save_button = None
        self.preview_button = None
        self.watermark_label = None
        self.watermark_entry = None

        self.config_main_ui()

    def config_main_ui(self):
        # root and mainframe
        self.root.title("Image Water marker")
        root = self.root
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        mainframe = ttk.Frame(root, padding="50 50 60 60")
        mainframe.grid(column=0, row=0)
        self.mainframe = mainframe

        # Buttons
        ttk.Button(mainframe, text="Open Image", command=self.load_image).grid(
            column=1, row=1, columnspan=2, sticky="ew"
        )

        preview_button = ttk.Button(
            mainframe, text="Preview Image", command=self.preview_watermark_img
        )
        preview_button.grid(column=1, row=5)
        save_button = ttk.Button(
            mainframe,
            text="Save Image",
            command=self.save_watermark_image,
        )
        save_button.grid(column=2, row=5)

        # Labels and images
        loaded_image_path_label = ttk.Label(mainframe, text="Add an image file")
        loaded_image_path_label.grid(column=1, row=2, columnspan=2, sticky="ew")
        loaded_image_preview_label = ttk.Label(mainframe)
        loaded_image_preview_label.grid(column=1, row=3, columnspan=2)
        # hide the label till its ready to be displayed
        loaded_image_path_label.grid_remove()
        loaded_image_preview_label.grid_remove()

        # watermark entry
        watermark_label = ttk.Label(mainframe, text="Watermark text:")
        watermark_label.grid(column=1, row=4)
        watermark_text = StringVar()
        watermark_entry = ttk.Entry(mainframe, width=20, textvariable=watermark_text)
        watermark_entry.grid(column=2, row=4)

        for child in mainframe.winfo_children():
            child.grid_configure(padx=5, pady=5)

        # hide the label till its ready to be displayed
        loaded_image_path_label.grid_remove()
        loaded_image_preview_label.grid_remove()
        # hide until watermark is previewed
        save_button.grid_remove()
        preview_button.grid_remove()
        watermark_label.grid_remove()
        watermark_entry.grid_remove()

        self.watermark_text = watermark_text
        self.save_button = save_button
        self.preview_button = preview_button
        self.loaded_image_path_label = loaded_image_path_label
        self.loaded_image_preview_label = loaded_image_preview_label
        self.watermark_label = watermark_label
        self.watermark_entry = watermark_entry

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
            self.loaded_image_path_label.configure(text=f"file: {file_path}")
            self.loaded_image = ImageProcessor(file_path)

            # attribute added to keep this in memory so that image can be displayed
            img_copy = self.loaded_image.img.copy()
            img_copy.thumbnail((MAX_WIDTH, MAX_HEIGHT))
            self.tk_converted_image = ImageTk.PhotoImage(img_copy)
            self.loaded_image_preview_label["image"] = self.tk_converted_image

            # display relevant buttons and labels
            self.enable_ui_after_load()
        else:
            print("No file selected")

    def save_watermark_image(self):
        if not self.loaded_image.watermarked_img:
            return
        watermarked_img_name = self.loaded_image.save_watermarked_img()
        messagebox.showinfo(
            "Saved", f"Watermarked image saved as {watermarked_img_name}"
        )

    def enable_ui_after_load(self):
        self.loaded_image_path_label.grid()
        self.loaded_image_preview_label.grid()
        self.save_button.grid()
        self.preview_button.grid()
        self.watermark_label.grid()
        self.watermark_entry.grid()

    def preview_watermark_img(self):
        self.loaded_image.watermark(self.watermark_text.get())

        # attribute added to keep this in memory so that image can be displayed
        self.loaded_image.watermark(self.watermark_text.get())
        img_copy = self.loaded_image.watermarked_img.copy()
        img_copy.thumbnail((MAX_WIDTH, MAX_HEIGHT))
        self.tk_converted_image = ImageTk.PhotoImage(img_copy)
        self.loaded_image_preview_label["image"] = self.tk_converted_image

        self.enable_ui_after_load()
