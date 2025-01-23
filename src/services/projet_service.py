from utils.json_helper import JSONHelper
from models.projet import Projet

class ProjetService:
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
        self.projets = JSONHelper.lire_json(self.fichier_json)

    def ajouter_projet(self, projet):
        """
        Ajoute un nouveau projet au fichier JSON.

        Args:
            projet (Projet): Le projet à ajouter.

        Returns:
            None
        """
        self.projets.append(projet.to_dict())
        self.sauvegarder_projets()

    def lister_projets(self):
        """
        Liste tous les projets stockés.

        Returns:
            list[Projet]: Une liste d'objets `Projet`.
        """
        return [Projet.from_dict(projet_data) for projet_data in self.projets]

    def sauvegarder_projets(self):
        """
        Sauvegarde la liste actuelle des projets dans le fichier JSON.

        Returns:
            None
        """
        JSONHelper.ecrire_json(self.fichier_json, self.projets)

    def supprimer_projet(self, projet_id):
        """
        Supprime un projet du fichier JSON en fonction de son ID.

        Args:
            projet_id (str | int): L'ID du projet à supprimer.

        Returns:
            bool: True si un projet a été supprimé, False sinon.
        """
        projets_avant = len(self.projets)
        self.projets = [projet for projet in self.projets if projet["id"] != projet_id]
        if len(self.projets) < projets_avant:
            self.sauvegarder_projets()
            return True
        return False
    def update_projet(self, projet):
        """
        Met à jour un projet existant dans le fichier JSON.

        Args:
            projet (Projet): Le projet contenant les nouvelles données.

        Raises:
            ValueError: Si le projet à mettre à jour n'existe pas.

        Returns:
            None
        """
        for i, p in enumerate(self.projets):
            if p["id"] == projet.id:
                self.projets[i] = projet.to_dict()
                self.sauvegarder_projets()
                return
        raise ValueError(f"Aucun projet avec l'ID {projet.id} n'a été trouvé.")
    def ajouter_user_au_projet(self, projet_id, user_id):
        """
        Ajoute un utilisateur à un projet.

        Args:
            projet_id (str): L'ID du projet.
            user_id (str): L'ID de l'utilisateur.

        Returns:
            None

        Raises:
            ValueError: Si le projet n'est pas trouvé.
        """
        for projet_data in self.projets:
            if projet_data["id"] == projet_id:
                if user_id not in projet_data["users"]:
                    projet_data["users"].append(user_id)
                    self.sauvegarder_projets()
                return
        raise ValueError(f"Aucun projet avec l'ID {projet_id} n'a été trouvé.")
    def supprimer_user_du_projet(self, projet_id, user_id):
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
        for projet_data in self.projets:
            if projet_data["id"] == projet_id:
                if user_id in projet_data["users"]:
                    projet_data["users"].remove(user_id)
                    self.sauvegarder_projets()
                    return True
                else:
                    raise ValueError(f"L'utilisateur avec l'ID {user_id} n'est pas associé au projet.")
        raise ValueError(f"Aucun projet avec l'ID {projet_id} n'a été trouvé.")
