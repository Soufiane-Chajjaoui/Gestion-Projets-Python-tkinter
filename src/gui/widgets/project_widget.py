import customtkinter as ctk
from PIL import Image, ImageTk
from gui.widgets.separator_widget import SeparatorWidget

class ProjectWidget(ctk.CTkFrame):
    def __init__(self, parent, project_id, project_name, project_description, delete_callback, add_user_project_callback):
        super().__init__(parent)
        self.project_id = project_id
        self.project_name = project_name
        self.project_description = project_description
        self.delete_callback = delete_callback
        self.add_user_project_callback = add_user_project_callback
        self.separator = None  # Ajoutez cette ligne pour stocker le séparateur
        # Charger les icônes avec une taille adaptée
        icon_size = (24, 24)  # Ajustez la taille des icônes
        
        self.group_icon = ctk.CTkImage(light_image=Image.open("D:/Dev/Gestion-Projets-Python-tkinter/assets/group-users.png"))
        self.delete_icon = ctk.CTkImage(light_image=Image.open("D:/Dev/Gestion-Projets-Python-tkinter/assets/trash-icon.png"))
        self.user_plus_icon = ctk.CTkImage(light_image=Image.open("D:/Dev/Gestion-Projets-Python-tkinter/assets/user-plus.png"))
        self.task_plus_icon = ctk.CTkImage(light_image=Image.open("D:/Dev/Gestion-Projets-Python-tkinter/assets/task-icon.png"))
        # Configurez le widget ici
        self.create_widget()

    def create_widget(self):
        """
        Crée l'interface pour afficher le projet.
        """
        # Nom du projet
        label_name = ctk.CTkLabel(self, text=self.project_name, font=("Arial", 16))
        label_name.pack(anchor="w", padx=10, pady=5)

        # Description du projet
        label_desc = ctk.CTkLabel(self, text=self.project_description, font=("Arial", 12), wraplength=300)
        label_desc.pack(anchor="w", padx=10, pady=5)

        # Boutons avec icônes
        button_frame = ctk.CTkFrame(self, fg_color="transparent")  # Cadre pour organiser les boutons
        button_frame.pack(anchor="e", padx=10, pady=5, fill="x")

        # Bouton de suppression
        delete_button = ctk.CTkButton(button_frame, image=self.delete_icon, text="", width=30, height=30, command=self.on_delete)
        delete_button.pack(side="right", padx=5)

        # Bouton d'ajout utilisateur
        user_plus_button = ctk.CTkButton(button_frame, image=self.user_plus_icon, text="", width=30, height=30, command=self.on_add_user)
        user_plus_button.pack(side="right", padx=5)

        # Bouton d'ajout tâche
        task_plus_button = ctk.CTkButton(button_frame, image=self.task_plus_icon, text="", width=30, height=30, command=self.on_add_task)
        task_plus_button.pack(side="right", padx=5)

    def on_delete(self):
        """
        Appelé lorsque le bouton 'Supprimer' est cliqué.
        """
        if self.delete_callback:
            self.delete_callback(self)

    def on_add_user(self):
        """
        Appelé lorsque le bouton 'Ajouter utilisateur' est cliqué.
        """
        if self.add_user_project_callback:
            self.add_user_project_callback(self)

    def on_add_task(self):
        """
        Appelé lorsque le bouton 'Ajouter tâche' est cliqué.
        """
        if self.update_callback:
            self.update_callback(self)