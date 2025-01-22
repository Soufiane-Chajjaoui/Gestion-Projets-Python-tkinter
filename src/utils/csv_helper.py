import csv

class CSVHelper:
    @staticmethod
    def lire_csv(fichier):
        try:
            with open(fichier, mode='r', newline='', encoding='utf-8') as f:
                return list(csv.reader(f))
        except FileNotFoundError:
            return []  # Retourne une liste vide si le fichier n'existe pas

    @staticmethod
    def ecrire_csv(fichier, donnees):
        with open(fichier, mode='w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerows(donnees)
