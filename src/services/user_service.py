from utils.json_helper import JSONHelper
from models.user import User

class UserService:
    """
    Service pour gérer les opérations sur les utilisateurs, comme l'ajout, 
    la suppression et la lecture à partir d'un fichier JSON.
    """

    def __init__(self, fichier_json='../data/users.json'):
        """
        Initialise le service avec un fichier JSON pour stocker les utilisateurs.

        Args:
            fichier_json (str): Le chemin du fichier JSON contenant les utilisateurs.
        """
        self.fichier_json = fichier_json
        self.users = JSONHelper.lire_json(self.fichier_json)

    def ajouter_user(self, user):
        """
        Ajoute un nouvel utilisateur au fichier JSON.

        Args:
            user (User): L'utilisateur à ajouter.

        Returns:
            None
        """
        self.users.append(user.to_dict())
        self.sauvegarder_users()

    def lister_users(self):
        """
        Liste tous les utilisateurs stockés.

        Returns:
            list[User]: Une liste d'objets `User`.
        """
        return [User.from_dict(user_data) for user_data in self.users]

    def sauvegarder_users(self):
        """
        Sauvegarde la liste actuelle des utilisateurs dans le fichier JSON.

        Returns:
            None
        """
        JSONHelper.ecrire_json(self.fichier_json, self.users)

    def supprimer_user(self, user_id):
        """
        Supprime un utilisateur du fichier JSON en fonction de son ID.

        Args:
            user_id (str | int): L'ID de l'utilisateur à supprimer.

        Returns:
            bool: True si un utilisateur a été supprimé, False sinon.
        """
        users_avant = len(self.users)
        self.users = [user for user in self.users if user["id"] != user_id]
        if len(self.users) < users_avant:
            self.sauvegarder_users()
            return True
        return False
