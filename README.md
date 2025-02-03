# Gestion-Projets-Python-tkinter
Créer un système de gestion de projets permettant de gérer des tâches, des utilisateurs et des projets. 


### Explications des dossiers :

- **`src/models/`** : Contient les classes représentant les données principales (`Tache`, `Utilisateur`, etc.).
- **`src/services/`** : Inclut les services pour la gestion des modèles, comme la manipulation ou la persistance des données.
- **`src/controllers/`** : Responsable de la logique métier principale et des interactions entre les modèles et l'interface.
- **`src/gui/`** : Dossier pour les fichiers liés à l'interface graphique.
- **`src/utils/`** : Contient des fonctions utilitaires partagées.
- **`src/exceptions/`** : Dossier pour gérer les exceptions spécifiques à votre application.
- **`tests/`** : Conçu pour contenir les tests unitaires de votre application.
- **`requirements.txt`** : Liste des bibliothèques Python requises pour exécuter le projet.
- **`README.md`** : Documentation expliquant le projet.
- **`.gitignore`** : Définit les fichiers/dossiers à ignorer dans le contrôle de version.

## Comment lancer l'application

### Installation des dépendances

Assurez-vous d'abord d'avoir installé toutes les bibliothèques requises. Pour ce faire, exécutez la commande suivante à la racine du projet :

```bash
pip install -r requirements.txt
```
### Exécution de l'application

Rendez-vous dans le dossier `src` et exécutez la commande suivante pour lancer l'application :

```bash
python main.py
```