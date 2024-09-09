from color_processor import ColorProcessor
from ui import UI


if __name__ == "__main__":
    color_processor = ColorProcessor()
    color_processor.main()

    ui = UI()
    ui.start_ui()
