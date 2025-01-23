import json

class JSONHelper:
    """
    Une classe utilitaire pour lire et écrire des fichiers JSON.
    """

    @staticmethod
    def lire_json(fichier):
        """
        Lit un fichier JSON et retourne une liste ou un dictionnaire.

        Args:
            fichier (str): Le chemin du fichier JSON.

        Returns:
            list | dict: Les données JSON sous forme d'une liste ou d'un dictionnaire.
                         Retourne une liste vide si le fichier n'existe pas ou en cas d'erreur.
        """
        try:
            with open(fichier, mode='r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            # Si le fichier n'existe pas, retourner une liste vide
            return []
        except json.JSONDecodeError as e:
            print(f"Erreur lors de la lecture du JSON : {e}")
            return []

    @staticmethod
    def ecrire_json(fichier, donnees):
        """
        Écrit des données dans un fichier JSON.

        Args:
            fichier (str): Le chemin du fichier JSON.
            donnees (list | dict): Les données à écrire dans le fichier JSON.

        Returns:
            None
        """
        with open(fichier, mode='w', encoding='utf-8') as f:
            json.dump(donnees, f, indent=4, ensure_ascii=False)
