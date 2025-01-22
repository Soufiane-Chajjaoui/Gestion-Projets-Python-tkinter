from datetime import datetime

class User:
    """
    Classe représentant un utilisateur avec un ID, un nom, un email et un rôle.
    """

    def __init__(self, nom, email, role, user_id=None):
        """
        Initialise un utilisateur.

        Args:
            nom (str): Nom de l'utilisateur.
            email (str): Email de l'utilisateur.
            role (str): Rôle de l'utilisateur.
            user_id (str, optional): Identifiant unique de l'utilisateur. Généré automatiquement si non fourni.
        """
        self.id = user_id or self.generer_id_unique()
        self.nom = nom
        self.email = email
        self.role = role

    @staticmethod
    def generer_id_unique():
        """
        Génère un ID unique basé sur la date et l'heure actuelle.

        Returns:
            str: Identifiant unique sous la forme 'YYYYMMDDHHMMSSffffff'.
        """
        return datetime.now().strftime('%Y%m%d%H%M%S%f')

    def to_csv_row(self):
        """
        Convertit l'utilisateur en une liste pour l'écriture dans un fichier CSV.

        Returns:
            list: Liste représentant l'utilisateur.
        """
        return [self.id, self.nom, self.email, self.role]

    @staticmethod
    def from_csv_row(row):
        """
        Crée un utilisateur à partir d'une ligne CSV.

        Args:
            row (list): Liste représentant une ligne dans un fichier CSV.

        Returns:
            User: Instance d'utilisateur créée à partir de la ligne.
        """
        return User(user_id=row[0], nom=row[1], email=row[2], role=row[3])
