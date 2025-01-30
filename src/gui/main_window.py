import customtkinter as ctk
from .pages.home_page import HomePage
from .pages.project_page import ProjectPage

class MainWindow(ctk.CTk):
    """
    Fenêtre principale qui contient des pages navigables.
    """

    def __init__(self):
        super().__init__()

        # Configuration de la fenêtre principale
        self.title("Application Gestion de Projets")
        self.geometry("800x600")  # Taille initiale de la fenêtre
        self.resizable(False, False)  # Permet de redimensionner la fenêtre

        # Conteneur principal pour les frames/pages
        self.container = ctk.CTkFrame(self, corner_radius=0)
        self.container.pack(fill="both", expand=True)

        # Dictionnaire pour stocker les différentes pages
        self.frames = {}

        # Initialisation des pages
        for PageClass in (HomePage, ProjectPage):
            page_name = PageClass.__name__
            frame = PageClass(parent=self.container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # Configurer la grille du conteneur pour que chaque page occupe tout l'espace
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        # Afficher la page d'accueil par défaut
        self.show_frame("HomePage")

    def show_frame(self, page_name):
        """
        Affiche une page donnée en fonction de son nom.

        Args:
            page_name (str): Le nom de la page à afficher.
        """
        frame = self.frames[page_name]
        frame.tkraise()
