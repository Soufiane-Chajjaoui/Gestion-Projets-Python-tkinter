# from models.tache import Tache
from models.user import User
# from services.tache_service import TacheService
from services.user_service import UserService
from services.projet_service import ProjetService
from models.projet import Projet
import time

# Initialisation des services
# Initialisation du service utilisateur
user_service = UserService()
# Ajout de deux utilisateurs
# user_service.ajouter_user(User(nom="Alice", email="alice@example.com", role="Admin"))
# user_service.ajouter_user(User(nom="Bob", email="bob@example.com", role="User"))

# Suppression d'un utilisateur
# id_to_remove = user_service.lister_users()[0].id  # ID de "Alice"
# if user_service.supprimer_user(id_to_remove):
#     print(f"L'utilisateur avec ID {id_to_remove} a été supprimé.")
# else:
#     print(f"Aucun utilisateur trouvé avec ID {id_to_remove}.")

# Vérification de la liste après suppression
print("\nListe des utilisateurs restants :")
for user in user_service.lister_users():
        print(user.id)
# Création d'un utilisateur
user_s = User(nom="Soufiane", email="soufian@example.com", role="Manager")
user_service.ajouter_user(user_s)
time.sleep(2)
user_m = User(nom="Mahdi", email="mahdi@example.com", role="Developer")
user_service.ajouter_user(user_m)

# Création de projets
projet_service = ProjetService()

# Création d'un projet
projet1 = Projet(nom="Projet Beta", description="Projet pour la gestion des tâches.", users=[user_s.id, user_m.id])
projet_service.ajouter_projet(projet1)

# Liste des projets
print("Projets disponibles:")
for projet in projet_service.lister_projets():
    print(f"- {projet.nom}")
    for user in projet.users:
        print(f"User: {user}")
        
# Liste des utilisateurs
print("\nUtilisateurs disponibles:")
for user in user_service.lister_users():
    print(f"- {user.nom}, Email: {user.email}")



print(f"\nMise à jour du projet avec ID={projet1.id}...")
projet_modifie = Projet(projet_id=projet1.id, nom="Projet Alpha - Modifié", description="Nouvelle description", users=[user_s.id])
projet_service.update_projet(projet_modifie)

projet_service.ajouter_user_au_projet(projet_id=projet_service.lister_projets()[0].id, user_id=user_m.id)
projet_service.supprimer_user_du_projet(projet_id=projet_service.lister_projets()[0].id, user_id=user_m.id)


# Lister les projets après mise à jour
print("\nListe des projets après modification :")
for projet in projet_service.lister_projets():
    print(f"- {projet.nom}")
    for user in projet.users:
        print(f"User: {user}")



# Suppression d'un projet
# projet_service.supprimer_projet(projet1.id)

# Suppression d'un utilisateur
# user_service.supprimer_user(user.id)
