import csv

class CSVHelper:
    @staticmethod
    def lire_csv(fichier):
        """
        Lit un fichier CSV et retourne une liste de dictionnaires si le fichier a des en-têtes.
        """
        with open(fichier, mode='r', encoding='utf-8') as f:
            lecteur = csv.DictReader(f)
            return list(lecteur)

    @staticmethod
    def ecrire_csv(fichier, lignes, entetes=None):
        """
        Écrit dans un fichier CSV à partir d'une liste de dictionnaires.

        Args:
            fichier (str): Le chemin du fichier CSV.
            lignes (list): Liste de dictionnaires représentant les lignes.
            entetes (list): Liste des en-têtes à écrire dans le fichier.
        """
        with open(fichier, mode='w', newline='', encoding='utf-8') as f:
            if entetes:  # Vérifiez si des en-têtes sont fournis
                writer = csv.DictWriter(f, fieldnames=entetes)
                writer.writeheader()  # Écrit les en-têtes dans le fichier
            else:
                writer = csv.writer(f)
            writer.writerows(lignes)