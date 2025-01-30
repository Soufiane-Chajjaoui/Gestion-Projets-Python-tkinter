import customtkinter as ctk

class FieldFormWidget(ctk.CTkFrame):
    """Widget personnalisé pour un champ de formulaire avec label"""
    def __init__(self, parent, label_text, **kwargs):
        super().__init__(parent, fg_color="transparent", **kwargs)
        self.label = ctk.CTkLabel(self, 
                                text=label_text,
                                font=("Arial", 12))
        self.label.pack(anchor="w", padx=10)
        
        self.entry = ctk.CTkEntry(self,
                                width=300,
                                height=35,
                                corner_radius=8)
        self.entry.pack(fill="x", pady=3, padx=10)
    
    def get_value(self):
        """Retourne la valeur saisie nettoyée"""
        return self.entry.get().strip()
