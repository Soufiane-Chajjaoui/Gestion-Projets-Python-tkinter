import time
from .user import User
from .task import Task  # Assurez-vous d'importer la classe Task

class Projet:
    """
    Modèle représentant un projet.
    """

    def __init__(self, nom, description, users=[], tasks=None, projet_id=None):
        """
        Initialise un objet Projet.

        Args:
            projet_id (str | int): L'identifiant unique du projet.
                                   Si aucun ID n'est fourni, un DateTime.now() est généré automatiquement.
            nom (str): Le nom du projet.
            description (str): La description du projet.
            users ([UserID]): Les utilisateurs associés au projet.
            tasks ([Task]): Liste des tâches associées au projet (par défaut, vide si non fourni).
        """
        self.id = projet_id if projet_id else int(time.time() * 1000)
        self.nom = nom
        self.description = description
        self.users = users  # Liste des utilisateurs associés au projet (par exemple, des IDs d'utilisateurs)
        self.tasks = tasks if tasks else []  # Liste des tâches (par défaut vide)

    def to_dict(self):
        """
        Convertit l'objet Projet en dictionnaire.

        Returns:
            dict: Représentation du projet sous forme de dictionnaire.
        """
        return {
            "id": self.id,
            "nom": self.nom,
            "description": self.description,
            "users": self.users,
            "tasks": [task.to_dict() for task in self.tasks],  # Convertit chaque tâche en dictionnaire
        }

    @classmethod
    def from_dict(cls, data):
        """
        Crée un objet Projet à partir d'un dictionnaire.

        Args:
            data (dict): Les données du dictionnaire.

        Returns:
            Projet: L'objet Projet créé.
        """
        tasks = [Task.from_dict(task_data) for task_data in data.get("tasks", [])]  # Convertir les tâches de dict à objets Task
        return cls(
            projet_id=data["id"],
            nom=data["nom"],
            description=data["description"],
            users=data["users"],
            tasks=tasks
        )
