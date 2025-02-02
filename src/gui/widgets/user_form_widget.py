from PIL import Image, ImageTk  # Pour gérer les icônes
from services.project_service import ProjectService
from services.user_service import UserService
from gui.widgets.user_widget import UserWidget
from gui.pages.task_page import TaskPage
from gui.widgets.field_form_widget import FieldFormWidget
from models.user import User
from models.projet import Projet
import customtkinter as ctk

class UserFormWidget(ctk.CTkToplevel):
    def __init__(self, parent, projectWidget, add_user_callback):
        super().__init__(parent)
        self.projectWidget = projectWidget
        self.add_user_callback = add_user_callback

        # Configuration de la fenêtre
        self.title("Gestion des Utilisateurs")
        self.geometry("800x500")
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.projectService = ProjectService()
        self.userService = UserService()
        self.users_widgets = []
        self.users = []

        # Charger les icônes nécessaires
        self.delete_icon = ctk.CTkImage(
            light_image=Image.open("D:/Dev/Gestion-Projets-Python-tkinter/assets/trash-icon.png"),
            size=(20, 20)
        )
        self.task_icon = ctk.CTkImage(
            light_image=Image.open("D:/Dev/Gestion-Projets-Python-tkinter/assets/task-icon.png"),
            size=(20, 20)
        )

        # Panneau de gauche pour la liste des utilisateurs
        self.create_user_list_panel()

        # Panneau de droite pour le formulaire
        self.create_form_panel()

    def create_user_list_panel(self):
        # Cadre pour la liste des utilisateurs
        list_frame = ctk.CTkFrame(self, width=300)
        list_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        
        # Titre de la liste
        ctk.CTkLabel(
            list_frame, 
            text=f"Utilisateurs du Projet\n{self.projectWidget.project_name}",
            font=("Arial", 14, "bold")
        ).pack(pady=10)

        # Liste scrollable des utilisateurs
        self.scrollable_list = ctk.CTkScrollableFrame(list_frame)
        self.scrollable_list.pack(fill="both", expand=True, padx=5, pady=5)
        
        # Charger les utilisateurs existants
        self.list_users()

    def list_users(self):
        """Affiche la liste des utilisateurs avec le widget personnalisé"""
        users = self.projectService.getUsersOfProject(self.projectWidget.project_id)
        print(f"Nombre d'utilisateurs trouvés : {len(users)}")
        if not users:
            ctk.CTkLabel(
                self.scrollable_list,
                text="Aucun utilisateur associé à ce projet", 
                text_color="gray"
            ).pack(pady=10)
            return

        for user in users:
            userWidget = UserWidget(
                parent=self.scrollable_list,
                user=user,
                project=Projet(nom=self.projectWidget.project_name,description=self.projectWidget.project_description,projet_id=self.projectWidget.project_id),
                delete_icon=self.delete_icon,
                task_icon=self.task_icon,
                delete_callback=self.delete_user,
                # task_callback=self.open_task_page  # Callback pour naviguer vers la page de tâches
            )
            userWidget.pack(fill="x", pady=2, padx=5)
            self.users_widgets.append(userWidget)

    def create_form_panel(self):
        form_frame = ctk.CTkFrame(self)
        form_frame.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)
        
        ctk.CTkLabel(
            form_frame, 
            text="Ajouter un Utilisateur",
            font=("Arial", 16, "bold")
        ).pack(pady=20)

        # Utilisation du FieldFormWidget pour les champs de saisie
        self.field_name = FieldFormWidget(form_frame, "Nom de l'utilisateur :")
        self.field_name.pack(pady=8, fill="x")
        
        self.field_email = FieldFormWidget(form_frame, "Email de l'utilisateur :")
        self.field_email.pack(pady=8, fill="x")
        
        self.field_role = FieldFormWidget(form_frame, "Rôle de l'utilisateur :")
        self.field_role.pack(pady=8, fill="x")

        submit_button = ctk.CTkButton(
            form_frame,
            text="Ajouter à ce Projet",
            command=self.on_submit,
            fg_color="#4CAF50",
            hover_color="#45a049"
        )
        submit_button.pack(pady=20)

    def on_submit(self):
        name = self.field_name.get_value()
        email = self.field_email.get_value()
        role = self.field_role.get_value()

        if all([name, email, role]):
            new_user = User(nom=name, email=email, role=role)
            self.add_user_callback(self.projectWidget, new_user)
            userWidget = UserWidget(
                parent=self.scrollable_list,
                user=new_user,
                project=self.projectWidget,
                delete_icon=self.delete_icon,
                task_icon=self.task_icon,
                delete_callback=self.delete_user,
                # task_callback=self.open_task_page  # Passage du callback pour la navigation
            )
            print(f"Ajout de l'utilisateur : {new_user.nom}")
            self.users_widgets.append(userWidget)
            userWidget.pack(fill="x", pady=2, padx=5)
        else:
            self.show_snackbar("Tous les champs doivent être remplis !", color="#FF0000")

    def delete_user(self, userWidget):
        # 1. Supprimer depuis le backend
        self.projectService.supprimer_user_du_projet(self.projectWidget.project_id, userWidget.user.id)
        self.userService.supprimer_user(userWidget.user.id)
        print(f"user {userWidget.user.id} supprimé du projet {self.projectWidget.project_id}")
        self.users_widgets.remove(userWidget)
        userWidget.destroy()
        if len(self.users_widgets) == 0:
            self.list_users()
        self.show_snackbar("Utilisateur bien supprimé")

    def show_snackbar(self, message, color="#008000"):
        snackbar = ctk.CTkFrame(self, fg_color=color, corner_radius=10)  # Couleur selon Material Design
        snackbar.place(relx=0.5, rely=0.05, anchor="center")  # Position en haut, centré horizontalement

        label = ctk.CTkLabel(snackbar, 
                             text=message, 
                             text_color="white",
                             font=("Arial", 12))
        label.pack(padx=20, pady=10)
        self.after(3000, snackbar.destroy)
