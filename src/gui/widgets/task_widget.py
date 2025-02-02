import customtkinter as ctk
from PIL import Image

class TaskWidget(ctk.CTkFrame):
    STATUS_COLORS = {
        "to do": "#F44336",       # Rouge (Must Have)
        "in progress": "#FF9800", # Orange (Should Have)
        "done": "#4CAF50"         # Vert (Could Have)
    }

    def __init__(self, parent, task, delete_callback=None, update_callback=None):
        """
        Widget sous forme de carte entièrement colorée en fonction du statut MoSCoW.

        Args:
            parent: Le widget parent.
            task: Un objet Task représentant la tâche, qui possède les attributs 'id', 'title', 'description' et 'status'.
            delete_callback: Fonction callback appelée pour supprimer la tâche.
            update_callback: Fonction callback appelée pour mettre à jour la tâche.
        """
        # Déterminer la couleur de fond en fonction du statut
        status_color = self.STATUS_COLORS.get(task.status, "#9E9E9E")  # Gris par défaut

        super().__init__(parent, corner_radius=10, fg_color=status_color)
        
        self.task = task
        self.delete_callback = delete_callback
        self.update_callback = update_callback

        # Charger les icônes nécessaires
        self.delete_icon = ctk.CTkImage(
            light_image=Image.open("D:/Dev/Gestion-Projets-Python-tkinter/assets/trash-icon.png"),
            size=(20, 20)
        )
        self.pen_icon = ctk.CTkImage(
            light_image=Image.open("D:/Dev/Gestion-Projets-Python-tkinter/assets/pen-icon.png"),
            size=(20, 20)
        )

        # Contenu de la carte
        content_frame = ctk.CTkFrame(self, fg_color=status_color)
        content_frame.pack(padx=10, pady=10, fill="both", expand=True)

        self.title_label = ctk.CTkLabel(content_frame, text=task.title, font=("Arial", 14, "bold"),
                                        text_color="white")
        self.title_label.pack(anchor="w")

        self.desc_label = ctk.CTkLabel(content_frame, text=task.description, font=("Arial", 12),
                                       text_color="white")
        self.desc_label.pack(anchor="w")

        self.status_label = ctk.CTkLabel(content_frame, text=f"Statut : {task.status}", font=("Arial", 12, "italic"),
                                         text_color="white")
        self.status_label.pack(anchor="w")

        # Boutons d'action dans un cadre dédié
        button_frame = ctk.CTkFrame(self, fg_color=status_color)
        button_frame.pack(fill="x", pady=5)

        # Bouton Modifier
        update_button = ctk.CTkButton(
            button_frame,
            text="Modifier",
            fg_color="white",
            image=self.pen_icon,
            hover_color="#E0E0E0",
            text_color="green",
            command=lambda: self.on_update_task()
        )
        update_button.pack(side="left", padx=5, expand=True)

        # Bouton Supprimer
        delete_button = ctk.CTkButton(
            button_frame,
            text="Supprimer",
            fg_color="white",
            image=self.delete_icon,
            hover_color="#E0E0E0",
            text_color="red",
            command=lambda: self.on_delete_task()
        )
        delete_button.pack(side="right", padx=5, expand=True)

    def on_delete_task(self):
        print(f"[Debug] Bouton Supprimer cliqué pour la tâche {self.task.id}")
        if self.delete_callback:
            self.delete_callback(self.task)
        else:
            print("[Erreur] Aucun callback de suppression défini!")

    def on_update_task(self):
        print(f"[Debug] Bouton Modifier cliqué pour la tâche {self.task.id}")
        if self.update_callback:
            self.update_callback(self.task)
        else:
            print("[Erreur] Aucun callback de modification défini!")
