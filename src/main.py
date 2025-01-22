# from models.tache import Tache
from models.user import User
# from services.tache_service import TacheService
from services.user_service import UserService

# Initialisation des services
# Initialisation du service utilisateur
user_service = UserService()
# Ajout de deux utilisateurs
user_service.ajouter_user(User(nom="Alice", email="alice@example.com", role="Admin"))
user_service.ajouter_user(User(nom="Bob", email="bob@example.com", role="User"))

# Suppression d'un utilisateur
id_to_remove = user_service.lister_users()[0].id  # ID de "Alice"
if user_service.supprimer_user(id_to_remove):
    print(f"L'utilisateur avec ID {id_to_remove} a été supprimé.")
else:
    print(f"Aucun utilisateur trouvé avec ID {id_to_remove}.")

# Vérification de la liste après suppression
print("\nListe des utilisateurs restants :")
for user in user_service.lister_users():
        print(user.id)
