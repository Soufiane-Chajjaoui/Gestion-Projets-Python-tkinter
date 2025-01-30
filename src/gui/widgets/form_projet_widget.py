from models.projet import Projet
import customtkinter as ctk

class FormProjetWidget(ctk.CTkFrame):
    def __init__(self, parent, add_project_callback):
        """
        Initialise le formulaire pour ajouter un projet.
        :param parent: Le parent pour ce widget (par exemple, ProjetPage).
        :param add_project_callback: Une fonction de rappel pour ajouter un projet.
        """
        super().__init__(parent)

        self.add_project_callback = add_project_callback

        # Configuration de la grille
        self.grid_columnconfigure(0, weight=1)

        # Champ pour le nom du projet avec fond gris
        self.name_entry = ctk.CTkEntry(self, placeholder_text="Nom du projet", fg_color="#3d3d3c")  # Fond gris
        self.name_entry.grid(row=0, column=0, sticky="ew", padx=10, pady=5)

        # Champ pour la description du projet avec Textbox (fond gris)
        self.desc_textbox = ctk.CTkTextbox(self, height=100, width=30, border_width=1, 
                                           fg_color="#3d3d3c")  # Fond gris
        self.desc_textbox.grid(row=1, column=0, sticky="ew", padx=10, pady=5)
        self.desc_textbox.insert("1.0", "Description du projet...")  # Placeholder pour la description
        self.desc_textbox.configure(state="disabled")  # Empêche l'édition du placeholder au début

        # Bouton pour ajouter le projet
        add_button = ctk.CTkButton(self, text="Ajouter Projet", command=self.on_add_project)
        add_button.grid(row=3, column=0, padx=10, pady=10, sticky="ew")

        # Rendre le Textbox modifiable une fois que l'utilisateur commence à taper
        self.desc_textbox.bind("<FocusIn>", self.on_focus_in)

    def on_focus_in(self, event):
        """
        Efface le placeholder lorsque l'utilisateur clique dans la zone de texte.
        """
        current_text = self.desc_textbox.get("1.0", "end-1c")
        if current_text == "Description du projet...":
            self.desc_textbox.delete("1.0", "end-1c")
            self.desc_textbox.configure(state="normal")

    def on_add_project(self):
        """
        Récupère les données des champs et appelle la fonction de rappel pour ajouter un projet.
        """
        name = self.name_entry.get().strip()
        description = self.desc_textbox.get("1.0", "end-1c").strip()  # Récupérer tout le texte du textbox

        # Vérifier que tous les champs sont remplis
        if not name or not description or description == "Description du projet...":
            # Afficher un message d'erreur si les champs sont vides
            print("Veuillez remplir tous les champs.")
            return

        # Appeler le callback pour ajouter un projet
        self.add_project_callback(Projet(nom=name, description=description, users=[]))  # Ajouter le rôle comme paramètre

        # Effacer les champs après l'ajout
        self.name_entry.delete(0, ctk.END)
        self.desc_textbox.delete("1.0", ctk.END)  # Effacer le texte du textbox
        self.desc_textbox.insert("1.0", "Description du projet...")  # Réinitialiser le placeholder
        self.desc_textbox.configure(state="disabled")  # Désactiver l'édition du placeholder
