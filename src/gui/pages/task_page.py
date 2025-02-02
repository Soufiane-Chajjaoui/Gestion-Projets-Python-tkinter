import customtkinter as ctk
from services.task_service import TaskService
from models.task import Task
from gui.widgets.field_form_widget import FieldFormWidget
from gui.widgets.task_widget import TaskWidget  # Assurez-vous que TaskWidget est dans ce module
from gui.widgets.form_task_widget import FormTaskWidget  # Importez le widget créé précédemment

class TaskPage(ctk.CTkToplevel):
    def __init__(self, parent, user, project, return_callback=None, **kwargs):
        """
        Crée un widget Frame pour afficher la page des tâches.

        Args:
            parent: Le widget parent dans lequel sera intégrée la page.
            user: L'utilisateur concerné (pour l'affichage, par exemple "Tâches pour ...").
            project: Le projet concerné (pour l'association des tâches).
            return_callback: Fonction callback à appeler lorsqu'on clique sur "Retour".
        """
        super().__init__(parent, **kwargs)
        self.user = user
        self.project = project
        self.return_callback = return_callback
        self.tasks = []         

        self.geometry("800x500")
        self.title("Gestion du Taches")
        # Configuration de la grille pour diviser la page en deux colonnes
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Partie gauche : liste des tâches
        list_frame = ctk.CTkFrame(self)
        list_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        ctk.CTkLabel(list_frame,
                     text=f"Tâches Affecte a {user.nom} du projet {project.nom}",
                     font=("Arial", 16, "bold")).pack(pady=10)

        self.scrollable_tasks = ctk.CTkScrollableFrame(list_frame)
        self.scrollable_tasks.pack(fill="both", expand=True, padx=5, pady=5)
        self.refresh_tasks_list()

        # Partie droite : formulaire d'ajout de tâche (widget isolé)
        form_task_widget = FormTaskWidget(self, submit_callback=self.on_submit_task)
        form_task_widget.grab_set()
        form_task_widget.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

        # Bouton Retour en bas de la page
        back_button = ctk.CTkButton(self,
                                    text="Retour",
                                    command=self.on_return,
                                    fg_color="#2196F3",
                                    hover_color="#1976D2")
        back_button.grid(row=1, column=0, columnspan=2, pady=10)

    def refresh_tasks_list(self):
        """Vide et rafraîchit l'affichage de la liste des tâches."""
        for widget in self.scrollable_tasks.winfo_children():
            widget.destroy()
            
        self.tasks = TaskService.get_task_By_user_id_And_project_id(self.user.id,self.project.id)  # Vous pourrez initialiser ou récupérer la liste des tâches depuis votre backend
        
        if not self.tasks:
            ctk.CTkLabel(self.scrollable_tasks,
                         text="Aucune tâche pour le moment.",
                         text_color="gray").pack(pady=10)
        else:
            for task in self.tasks:
                task_widget = TaskWidget(self.scrollable_tasks, task,
                                         delete_callback=self.delete_task,
                                         update_callback=self.update_task)
                task_widget.pack(fill="x", pady=5, padx=5)

    def on_submit_task(self, title, description, status):
        """Callback appelé par le formulaire pour ajouter une nouvelle tâche."""
        new_task = Task(title, description, status , self.user.id, self.project.id)
        TaskService.add_task(new_task)
        self.tasks.append(new_task)
        self.refresh_tasks_list()

    def delete_task(self, task):
        """Supprime une tâche et rafraîchit la liste."""
        print("Deleting task")
        TaskService.delete_task(task.id)
        self.refresh_tasks_list()

    def update_task(self, task):
        """Exemple de callback pour mettre à jour une tâche."""
        print(f"Mettre à jour la tâche : {task}")

    def on_return(self):
        """
        Marche pas !!!
        """
        print("Tentative de fermeture de la fenêtre avec quit()")
        self.destroy()
