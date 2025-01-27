import customtkinter as ctk
from PIL import Image , ImageTk

class HomePage(ctk.CTkFrame):
    """
    Page d'accueil avec une image qui occupe toute la fenêtre.
    """

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        # Configurer le frame pour occuper tout l'espace disponible
        self.grid(row=0, column=0, sticky="nsew")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Charger l'image d'arrière-plan
        self.original_image = Image.open("D:/Dev/Gestion-Projets-Python-tkinter/assets/person-task.jpg")
        self.bg_image = ImageTk.PhotoImage(self.original_image)

        # Ajouter l'image d'arrière-plan
        self.bg_label = ctk.CTkLabel(self, image=self.bg_image, text="")
        self.bg_label.place(relwidth=1, relheight=1)

        # Titre
        self.title_label = ctk.CTkLabel(
            self,
            text="Bienvenue sur l'application de Gestion de Projets",
            font=ctk.CTkFont(size=28, weight="bold"),
            text_color="white"
        )
        self.title_label.place(relx=0.5, rely=0.3, anchor="center")

        # Bouton pour naviguer vers la page Projet
        self.get_started_button = ctk.CTkButton(
            self,
            text="Commencer",
            font=ctk.CTkFont(size=18),
            command=lambda: controller.show_frame("ProjectPage"),
            fg_color="#1D3557",
            hover_color="#457B9D",
            text_color="white",
            width=200,
        )
        self.get_started_button.place(relx=0.5, rely=0.6, anchor="center")

        # Ajuster l'image lorsque la fenêtre est redimensionnée
        self.bind("<Configure>", self.resize_image)

    def resize_image(self, event):
        """
        Redimensionne l'image pour s'adapter à la taille de la fenêtre en remplissant tout l'espace.
        """
        # Taille de la fenêtre
        new_width = event.width
        new_height = event.height

        # Taille originale de l'image
        original_width, original_height = self.original_image.size

        # Calcul du ratio pour remplir l'espace sans déformation
        ratio_width = new_width / original_width
        ratio_height = new_height / original_height

        # Choisir le ratio le plus grand pour s'assurer que l'image remplit la fenêtre
        ratio = max(ratio_width, ratio_height)

        # Calcul des nouvelles dimensions de l'image
        resized_width = int(original_width * ratio)
        resized_height = int(original_height * ratio)

        # Redimensionner l'image
        resized_image = self.original_image.resize((resized_width, resized_height), Image.ANTIALIAS)
        self.bg_image = ImageTk.PhotoImage(resized_image)
        self.bg_label.configure(image=self.bg_image)

        # Centrer l'image si elle dépasse la fenêtre
        self.bg_label.place(x=(new_width - resized_width) // 2, y=(new_height - resized_height) // 2)
