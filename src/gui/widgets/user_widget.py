from PIL import Image, ImageTk
from services.project_service import ProjectService
import customtkinter as ctk

class UserWidget(ctk.CTkFrame):
    """Widget personnalisé pour afficher un utilisateur"""
    def __init__(self, parent, user, delete_icon, task_icon, delete_callback):
        super().__init__(parent)
        self.user = user
        self.delete_callback = delete_callback
        
        # Configuration grid
        self.grid_columnconfigure(0, weight=1)  # Nom et rôle
        self.grid_columnconfigure(1, weight=1)  # Email
        self.grid_columnconfigure(2, weight=0)  # Icône delete
        self.grid_columnconfigure(3, weight=0)  # Icône task
        # Éléments d'interface
        self.create_widgets(delete_icon,task_icon)
        
    def create_widgets(self, delete_icon,task_icon):
        # Nom et rôle
        ctk.CTkLabel(self, 
                    text=f"• {self.user.nom} ({self.user.role})", 
                    anchor="w",
                    font=("Arial", 12)).grid(row=0, column=0, sticky="w", padx=(10, 5))
        
        # Email
        ctk.CTkLabel(self, 
                    text=self.user.email,
                    text_color="#808080",
                    anchor="e",
                    font=("Arial", 11, "italic")).grid(row=0, column=1, sticky="e", padx=(5, 10))

        # Bouton de suppression
        ctk.CTkButton(
            self,
            text="",
            image=delete_icon,
            width=30,
            height=30,
            fg_color="transparent",
            hover_color="#ffcccc",
            command=self.on_delete
        ).grid(row=0, column=2, sticky="e", padx=(10, 5))

        ctk.CTkButton(
            self,
            text="",
            image=task_icon,
            width=30,
            height=30,
            fg_color="transparent",
            hover_color="#ccccff",
            command=self.on_add_task
        ).grid(row=0, column=3, sticky="e", padx=(5, 5))

    def on_delete(self):
        """Gère la suppression de l'utilisateur"""
        if self.delete_callback:
            self.delete_callback(self)
            self.destroy()
    def on_add_task(self):
        