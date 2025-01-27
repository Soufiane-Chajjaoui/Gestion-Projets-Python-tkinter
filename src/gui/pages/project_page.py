import customtkinter as ctk
from gui.widgets.project_widget import ProjectWidget
from gui.widgets.form_projet_widget import FormProjetWidget
from gui.widgets.user_form_widget import UserFormWidget
from services.project_service import ProjectService
from services.user_service import UserService
from models.projet import Projet
from models.user import User



class ProjectPage(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.projectService = ProjectService()
        self.userService = UserService()

        # Configurer la mise en page
        self.grid_columnconfigure(0, weight=1, minsize=400)  # Colonne de gauche (formulaire)
        self.grid_columnconfigure(1, weight=1, minsize=400)  # Colonne de droite (liste des projets)
        self.grid_rowconfigure(0, weight=1)  # Ligne 1 (formulaire et liste de projets)
        self.grid_rowconfigure(1, weight=0, minsize=40)  # Ligne 2 (boutons en bas)

        # Liste pour les widgets de projet
        self.project_widgets = []

        # Créez le conteneur pour afficher les projets
        self.project_list_frame = ctk.CTkScrollableFrame(self)
        self.project_list_frame.grid(row=0, column=1, sticky="nsew", padx=20, pady=10)  # Liste à droite

        # Ajouter le formulaire pour les projets
        self.create_form()

        # Ajouter les boutons en bas
        self.create_bottom_buttons()

        # Lister les projets existants
        self.lister_projects()
    def create_bottom_buttons(self):
        """
        Ajoute les boutons en bas (retour à l'accueil et liste des utilisateurs) avec un espacement.
        """
        # Bouton Retour à l'accueil
        back_button = ctk.CTkButton(
            self,
            text="Retour à l'accueil",
            command=self.go_to_home
        )
        back_button.grid(row=1, column=0, padx=(20, 10), pady=10, sticky="w")  # Espacement à droite

    def create_form(self):
        """
        Ajoute le formulaire pour saisir les informations de projet.
        """
        form_widget = FormProjetWidget(self, self.add_project)
        form_widget.grid(row=0, column=0, sticky="nsew", padx=20, pady=(20, 10))  # Formulaire à gauche
    def add_project(self, project_id, name, description):
        """
        Ajoute un widget projet dans la liste.
        """
        projectWidget = ProjectWidget(
            parent=self.project_list_frame,
            project_id= project_id,
            project_name=name,
            project_description=description,
            delete_callback=self.remove_project,
            add_user_project_callback=self.add_user_project
        )
        self.projectService.ajouter_projet(Projet(nom=name, description=description, users=[]))
        projectWidget.pack(fill="x", padx=10, pady=5)

        # Créer un séparateur avec couleur
        separator = ctk.CTkFrame(self.project_list_frame, height=2, corner_radius=0, bg_color="#D3D3D3")
        separator.pack(fill="x", padx=10, pady=5)

        # Associer le séparateur au projet
        projectWidget.separator = separator  # Ajoutez cette ligne
        # Stockez le widget dans la liste
        self.project_widgets.append(projectWidget)

    def remove_project(self, projectWidget):
        """
        Supprime un projet de la liste et affiche un snackbar.
        """
        # Supprime le projet du service et détruit le widget
        self.projectService.supprimer_projet(projectWidget.project_id)
        
        # Supprime le séparateur associé au projet
        if projectWidget.separator:
            projectWidget.separator.destroy()  # Supprime le séparateur

        # Détruit le widget du projet
        projectWidget.destroy()
        self.project_widgets.remove(projectWidget)
        
        # Affiche un snackbar confirmant la suppression
        self.show_snackbar(f"Le projet '{projectWidget.project_name}' a été supprimé avec succès.")

    def lister_projects(self):
        """
        Liste les projets existants.
        """
        print("Liste les projets existants")
        projects = self.projectService.lister_projets()
        for p in projects:
            print(p.id)
            projectWidget = ProjectWidget(
                parent=self.project_list_frame,
                project_id= p.id,
                project_name= p.nom,
                project_description= p.description,
                delete_callback=self.remove_project,
                add_user_project_callback=self.add_user_project
            )
            projectWidget.pack(fill="x", padx=10, pady=5)
            if p != (len(projects) - 1):
                # Créer un séparateur avec couleur
                separator = ctk.CTkFrame(self.project_list_frame, height=2, corner_radius=0, bg_color="#D3D3D3")
                separator.pack(fill="x", padx=10, pady=5)

                # Associer le séparateur au projet
                projectWidget.separator = separator  # Ajoutez cette ligne
            
            self.project_widgets.append(projectWidget)

    def go_to_home(self):
        """
        Retourne à l'accueil en appelant le contrôleur.
        """
        self.controller.show_frame("HomePage")  # Remplacez "HomePage" par le nom de la page d'accueil.

    def add_user_project(self, projectWidget):
        """
        Ouvre un formulaire pour ajouter un utilisateur à un projet spécifique.
        """
        user_form = UserFormWidget(self, projectWidget, self.add_user_to_project)
        user_form.grab_set()  # Rend la fenêtre modale
        # self.show_user_form(projectWidget)

        
    def show_snackbar(self, message):
        """
        Affiche un snackbar avec un message temporaire en haut de la fenêtre.
        """
        # Crée un cadre pour le snackbar avec un fond vert
        snackbar = ctk.CTkFrame(self, fg_color="#4CAF50", corner_radius=10)  # Vert (Material Design)
        snackbar.place(relx=0.5, rely=0.05, anchor="center")  # Position en haut, centré horizontalement

        # Ajoute un label pour afficher le message
        label = ctk.CTkLabel(snackbar, text=message, text_color="white", font=("Arial", 12))
        label.pack(padx=20, pady=10)

        # Masquer le snackbar après 3 secondes
        self.after(3000, snackbar.destroy)

    def add_user_to_project(self, projectWidget, name, email, role, form_frame):
        """
        Ajoute un utilisateur au projet après soumission du formulaire.
        """
        if name and email:
            # Ici, vous pouvez ajouter la logique pour lier l'utilisateur au projet
            print(f"Utilisateur ajouté : {name} ({email}) {role} au projet {projectWidget.project_id}")
            user_save = User(nom=name, email=email, role=role)
            self.userService.ajouter_user(user_save)
            print(f"{user_save.id}")
            self.projectService.ajouter_user_au_projet(projectWidget.project_id,user_save.id)
            # Fermer le formulaire après l'ajout
            form_frame.destroy()

            # Afficher un snackbar pour confirmer l'ajout
            self.show_snackbar(f"L'utilisateur '{name}' a été ajouté avec succès.")
        else:
            self.show_snackbar("Veuillez remplir tous les champs.")