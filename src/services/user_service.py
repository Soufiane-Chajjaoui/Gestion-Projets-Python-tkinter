from utils.csv_helper import CSVHelper
from models.user import User
import os

class UserService:
    """
    Service pour gérer les utilisateurs, incluant les opérations de sauvegarde,
    de lecture et de mise à jour dans un fichier CSV.

    Attributes:
        fichier_csv (str): Le chemin du fichier CSV pour stocker les utilisateurs.
        users (list): Liste des objets User.
    """
    
    def __init__(self, fichier_csv='../data/users.csv'):
        """
        Initialise le service utilisateur. Si le fichier CSV n'existe pas,
        il est créé avec des en-têtes par défaut.

        Args:
            fichier_csv (str): Chemin du fichier CSV pour stocker les utilisateurs.
        """
        self.fichier_csv = fichier_csv
        if not os.path.exists(self.fichier_csv):
            CSVHelper.ecrire_csv(self.fichier_csv, [], entetes=["ID", "Nom", "Email", "Rôle"])
        self.users = [User.from_csv_row(row) for row in CSVHelper.lire_csv(self.fichier_csv)]

    def ajouter_user(self, user):
        """
        Ajoute un utilisateur à la liste et met à jour le fichier CSV.

        Args:
            user (User): L'utilisateur à ajouter.
        """
        self.users.append(user)
        self.sauvegarder_users()

    def lister_users(self):
        """
        Retourne la liste de tous les utilisateurs.

        Returns:
            list: Liste des objets User.
        """
        return self.users

    def sauvegarder_users(self):
        """
        Sauvegarde tous les utilisateurs dans le fichier CSV.
        Écrase le contenu existant avec la liste actuelle des utilisateurs.
        """
        CSVHelper.ecrire_csv(self.fichier_csv, [user.to_csv_row() for user in self.users])
    
    def supprimer_user(self, user_id):
        """
        Supprime un utilisateur par son ID, si trouvé.

        Args:
            user_id (str): L'identifiant de l'utilisateur à supprimer.

        Returns:
            bool: True si l'utilisateur a été supprimé, False sinon.
        """
        users_avant = len(self.users)
        self.users = [user for user in self.users if user.id != user_id]
        if len(self.users) < users_avant:
            self.sauvegarder_users()
            return True
        return