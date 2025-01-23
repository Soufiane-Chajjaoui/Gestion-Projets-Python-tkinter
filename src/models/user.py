import uuid
import time
class User:
    """
    Modèle représentant un utilisateur.
    """

    def __init__(self, id=None, nom="", email="", role=""):
        """
        Initialise un objet User.

        Args:
            id (str | int, optional): L'identifiant unique de l'utilisateur. 
                                      Si aucun ID n'est fourni, un DateTime.now() est généré automatiquement.
            nom (str): Le nom de l'utilisateur.
            email (str): L'email de l'utilisateur.
            role (str): Le rôle de l'utilisateur.
        """
        self.id = id if id else int(time.time() * 1000)  # Génère un UUID si aucun ID n'est fourni
        self.nom = nom
        self.email = email
        self.role = role

    def to_dict(self):
        """
        Convertit l'objet User en dictionnaire.

        Returns:
            dict: Représentation de l'utilisateur sous forme de dictionnaire.
        """
        return {"id": self.id, "nom": self.nom, "email": self.email, "role": self.role}

    @classmethod
    def from_dict(cls, data):
        """
        Crée un objet User à partir d'un dictionnaire.

        Args:
            data (dict): Les données du dictionnaire.

        Returns:
            User: L'objet User créé.
        """
        return cls(
            id=data.get("id"),  # Utilise l'ID fourni ou None
            nom=data.get("nom", ""),
            email=data.get("email", ""),
            role=data.get("role", "")
        )
