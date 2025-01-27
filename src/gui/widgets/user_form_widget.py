import customtkinter as ctk

class UserFormWidget(ctk.CTkToplevel):
    def __init__(self, parent, projectWidget, add_user_callback):
        """
        Initialise le formulaire d'ajout d'utilisateur.

        Args:
            parent: La fenêtre parente.
            projectWidget: Le widget du projet associé.
            add_user_callback: La fonction de rappel pour ajouter un utilisateur.
        """
        super().__init__(parent)
        self.projectWidget = projectWidget
        self.add_user_callback = add_user_callback

        # Configuration de la fenêtre
        self.title("Ajouter un utilisateur")
        self.geometry("400x400")  # Ajuster les dimensions pour inclure le champ du rôle

        # Ajouter un label pour afficher le nom du projet associé
        project_label = ctk.CTkLabel(
            self,
            text=f"Projet associé : {self.projectWidget.project_name}",
            font=("Arial", 14, "bold"),
            text_color="#333"
        )
        project_label.pack(pady=(20, 10))  # Espacement en haut et en bas

        # Ajouter les champs du formulaire
        label_name = ctk.CTkLabel(self, text="Nom de l'utilisateur :", font=("Arial", 12))
        label_name.pack(pady=(10, 5))
        self.entry_name = ctk.CTkEntry(self, width=300)
        self.entry_name.pack(pady=5)

        label_email = ctk.CTkLabel(self, text="Email de l'utilisateur :", font=("Arial", 12))
        label_email.pack(pady=5)
        self.entry_email = ctk.CTkEntry(self, width=300)
        self.entry_email.pack(pady=5)

        # Ajouter un champ pour le rôle de l'utilisateur
        label_role = ctk.CTkLabel(self, text="Rôle de l'utilisateur :", font=("Arial", 12))
        label_role.pack(pady=5)
        self.entry_role = ctk.CTkEntry(self, width=300)
        self.entry_role.pack(pady=5)

        # Ajouter un bouton pour valider l'ajout
        submit_button = ctk.CTkButton(
            self,
            text="Ajouter",
            command=self.on_submit
        )
        submit_button.pack(pady=20)

    def on_submit(self):
        """
        Appelé lorsque le bouton 'Ajouter' est cliqué.
        """
        name = self.entry_name.get()
        email = self.entry_email.get()
        role = self.entry_role.get()  # Récupérer le rôle

        if name and email and role:  # Vérifier que tous les champs sont remplis
            # Appeler la fonction de rappel pour ajouter l'utilisateur
            self.add_user_callback(self.projectWidget, name, email, role, self)
        else:
            # Afficher un message d'erreur si les champs sont vides
            self.show_error("Veuillez remplir tous les champs.")

    def show_error(self, message):
        """
        Affiche un message d'erreur dans un snackbar.

        Args:
            message (str): Le message d'erreur à afficher.
        """
        error_label = ctk.CTkLabel(self, text=message, text_color="red", font=("Arial", 12))
        error_label.pack(pady=10)
        self.after(3000, error_label.destroy)  # Masquer le message après 3 secondes