import customtkinter as ctk
from gui.main_window import MainWindow

if __name__ == "__main__":
    ctk.set_appearance_mode("dark")  # Mode sombre
    ctk.set_default_color_theme("blue")  # Thème par défaut

    app = MainWindow()
    app.mainloop()