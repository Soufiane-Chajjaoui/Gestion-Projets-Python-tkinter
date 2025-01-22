# Gestion-Projets-Python-tkinter
Créer un système de gestion de projets permettant de gérer des tâches, des utilisateurs et des projets. 

voila structure de ce projet
gestion-projets-python-tkinter/
│
├── src/
│   ├── models/                # Contient les modèles
│   │   ├── __init__.py
│   │   ├── tache.py           # Classe Tache
│   │   └── utilisateur.py     # Classe Utilisateur
│   ├── services/              # Services pour gérer les modèles
│   │   ├── __init__.py
│   │   ├── tache_service.py   # Service pour Tache
│   │   └── utilisateur_service.py  # Service pour Utilisateur
│   ├── controllers/           # Logique de l'application
│   │   ├── __init__.py
│   │   └── app_controller.py  # Contrôleur principal
│   ├── gui/                   # Interface graphique
│   └── utils/                 # Fonctions utilitaires
│   └── exceptions/            # Gestion des exceptions
│
├── tests/                     # Tests unitaires
├── requirements.txt           # Liste des dépendances
├── README.md                  # Documentation du projet
├── .gitignore                 # ignore fichiers ou bien dossiers du projet