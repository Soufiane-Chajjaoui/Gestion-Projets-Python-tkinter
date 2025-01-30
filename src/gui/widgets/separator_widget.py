import customtkinter as ctk

class SeparatorWidget(ctk.CTkFrame):
    def __init__(self, parent, **kwargs):
        super().__init__(parent, **kwargs)
        self.configure(height=2, bg_color="#949699")  # Définir la couleur et la hauteur du séparateur
        self.grid_rowconfigure(0, weight=1)
