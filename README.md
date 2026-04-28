
# 1. Ouvrir le projet
cd bibliotheque_project

# 2. Créer l'environnement virtuel
python -m venv venv

# 3. Activer l'environnement virtuel
venv\Scripts\activate

# 4. Installer les dépendances
pip install -r requirements.txt

# 5. Appliquer les migrations
python manage.py migrate

# 6. Créer un superutilisateur
python manage.py createsuperuser

# 7. (Optionnel) Ajouter des données de test
python seed_data.py

# 8. Lancer le serveur
python manage.py runserver
