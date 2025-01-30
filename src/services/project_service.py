from utils.json_helper import JSONHelper
from models.projet import Projet
from .user_service import UserService

class ProjectService:
    """
    Service pour gérer les opérations sur les projets, comme l'ajout, 
    la suppression et la lecture à partir d'un fichier JSON.
    """

    def __init__(self, fichier_json='../data/projets.json'):
        """
        Initialise le service avec un fichier JSON pour stocker les projets.

        Args:
            fichier_json (str): Le chemin du fichier JSON contenant les projets.
        """
        self.fichier_json = fichier_json
        self.projects = self.getProjects()
        self.userService = UserService()

    def ajouter_projet(self, project):
        """
        Ajoute un nouveau projet au fichier JSON.

        Args:
            projet (Projet): Le projet à ajouter.

        Returns:
            None
        """
        self.projects.append(project)
        self.save_projects()

    def getProjects(self):
        """
        Liste tous les projets stockés.

        Returns:
            list[Projet]: Une liste d'objets `Projet`.
        """
        return [Projet.from_dict(project_data) for project_data in JSONHelper.lire_json(self.fichier_json)]

    def save_projects(self):
        """
        Sauvegarde la liste actuelle des projets dans le fichier JSON.

        Returns:
            None
        """
        JSONHelper.ecrire_json(self.fichier_json, [p.to_dict() for p in self.projects])

    def supprimer_projet(self, project_id):
        """
        Supprime un projet du fichier JSON en fonction de son ID.

        Args:
            project_id (str | int): L'ID du projet à supprimer.

        Returns:
            bool: True si un projet a été supprimé, False sinon.
        """
        projects_avant = len(self.projects)
        self.projects = [p for p in self.projects if p.id != project_id]
        if len(self.projects) < projects_avant:
            self.save_projects()
            self.projects = self.getProjects()
            return True
        return False
    def update_project(self, project):
        """
        Met à jour un projet existant dans le fichier JSON.

        Args:
            projet (Projet): Le projet contenant les nouvelles données.

        Raises:
            ValueError: Si le projet à mettre à jour n'existe pas.

        Returns:
            None
        """
        for i, p in enumerate(self.projects):
            if p.id == project.id:
                self.projects[i] = project
                self.save_projects()
                return
        raise ValueError(f"Aucun projet avec l'ID {projet.id} n'a été trouvé.")
    def ajouter_user_au_projet(self, project_id, user_id):
        """
        Ajoute un utilisateur à un projet.

        Args:
            project_id (str): L'ID du projet.
            user_id (str): L'ID de l'utilisateur.

        Raises:
            ValueError: Si le projet n'est pas trouvé.
        """
        projects = self.getProjects()
        print(f"Projets récupérés : {[p.id for p in projects]}")  # Debug

        for p in projects:
            if p.id == project_id:
                if user_id not in p.users:
                    print(f"Users avant ajout : {p.users}")  # Debug
                    p.users.append(user_id)
                    print(f"Users après ajout : {p.users}")  # Debug
                    # Mettre à jour le projet dans la liste principale
                    self.update_project(p)
                    return

        raise ValueError(f"Aucun projet avec l'ID {project_id} n'a été trouvé.")  # Exception levée après la boucle

    def supprimer_user_du_projet(self, project_id, user_id):
        """
        Supprime un utilisateur d'un projet.

        Args:
            projet_id (str | int): L'ID du projet.
            user_id (str | int): L'ID de l'utilisateur à supprimer.

        Returns:
            bool: True si un utilisateur a été supprimé, False sinon.

        Raises:
            ValueError: Si le projet n'est pas trouvé.
        """
        if (p := self.getProject(project_id)):
            if user_id in p.users:
                p.users.remove(user_id)
                self.update_project(p)
                return True
            else:
                raise ValueError(f"L'utilisateur avec l'ID {user_id} n'est pas associé au projet.")
        raise ValueError(f"Aucun projet avec l'ID {project_id} n'a été trouvé.")
    def getUsersOfProject(self, project_id):
        # Récupérer les IDs utilisateurs du projet
        self.getProjects()
        project = self.getProject(project_id)
        if project:
            user_ids = project.users
            return self.userService.get_users(user_ids)
        return [] 
        
    def getProject(self, project_id):
        # Corriger le filtre et vérifier la structure des données
        projects = list(filter(lambda x: x.id == project_id, self.getProjects()))
        return projects[0] if projects else None