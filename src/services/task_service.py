from utils.json_helper import JSONHelper
from .user_service import UserService
from .project_service import ProjectService
from models.task import Task  # Assurez-vous d'importer la classe Task

class TaskService:
    fichier_json = '../data/tasks.json'  # Définition de l'attribut statique
    
    def __init__(self):
        self.userService = UserService()
        self.projectService = ProjectService()
    
    @staticmethod
    def get_task_By_user_id_And_project_id(user_id, project_id):
        """Méthode statique pour récupérer les tâches par user_id et project_id."""
        return list(filter(lambda t: t.user == user_id and t.project == project_id, TaskService.get_tasks()))
    
    @staticmethod
    def save_tasks(tasks):
        """Méthode statique pour sauvegarder plusieurs tâches."""
        JSONHelper.ecrire_json(TaskService.fichier_json, [task.to_dict() for task in tasks])

    @staticmethod
    def add_task(task):
        """Méthode statique pour ajouter une seule tâche."""
        tasks = TaskService.get_tasks()  # Charger les tâches existantes
        tasks.append(task)  # Ajouter la nouvelle tâche
        TaskService.save_tasks(tasks)  # Sauvegarder la nouvelle liste

    @staticmethod
    def get_tasks():
        """Méthode statique pour récupérer toutes les tâches."""
        return [Task.from_dict(t) for t in JSONHelper.lire_json(TaskService.fichier_json)]

    @staticmethod
    def delete_task(task_id):
        """
        Supprime une tâche du fichier JSON en fonction de son ID.

        Args:
            task_id (str | int): L'ID de la tâche à supprimer.

        Returns:
            bool: True si une tâche a été supprimée, False sinon.
        """
        tasks = TaskService.get_tasks()
        tasks_avant = len(tasks)
        tasks = [task for task in tasks if task.id != task_id]

        if len(tasks) < tasks_avant:
            TaskService.save_tasks(tasks)
            return True
        return False