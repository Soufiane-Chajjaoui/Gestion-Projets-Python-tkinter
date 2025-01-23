import time
from .user import User

class Projet:
    """
    Modèle représentant un projet.
    """

    def __init__(self, nom, description, users, projet_id=None):
        """
        Initialise un objet Projet.

        Args:
            projet_id (str | int): L'identifiant unique du projet.
                                   Si aucun ID n'est fourni, un DateTime.now() est généré automatiquement.
            nom (str): Le nom du projet.
            description (str): La description du projet.
            users ([UserID]): Les utilisateurs associé au projet.
        """
        self.id = projet_id if projet_id else int(time.time() * 1000)  
        self.nom = nom
        self.description = description
        self.users = users # Récupérer uniquement les ids des utilisateurs
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
        return cls(projet_id=data["id"], nom=data["nom"], description=data["description"], users=data["users"])
