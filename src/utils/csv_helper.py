import os
import csv

class CSVHelper:
    
    @staticmethod
    def ecrire_csv(fichier, data, entetes=None):
        """
        Écrit des données dans un fichier CSV avec option pour ajouter des en-têtes.

        :param fichier: Chemin du fichier CSV.
        :param data: Données à écrire (liste de listes).
        :param entetes: Liste des noms de colonnes (en-têtes).
        """
        # S'assurer que le dossier contenant le fichier existe
        os.makedirs(os.path.dirname(fichier), exist_ok=True)

        with open(fichier, mode='w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            if entetes:  # Écrire les en-têtes si fournis
                writer.writerow(entetes)
            writer.writerows(data)

    @staticmethod
    def lire_csv(fichier):
        """Lit un fichier CSV et retourne les lignes."""
        try:
            with open(fichier, mode='r', newline='', encoding='utf-8') as f:
                reader = csv.reader(f)
                return list(reader)
        except FileNotFoundError:
            return []