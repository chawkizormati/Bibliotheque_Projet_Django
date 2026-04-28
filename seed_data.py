import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from livres.models import Categorie, Livre

cats = ['Roman', 'Science-Fiction', 'Histoire', 'Informatique', 'Philosophie']
cat_objs = []
for nom in cats:
    c, _ = Categorie.objects.get_or_create(nom=nom)
    cat_objs.append(c)

livres = [
    ('Le Petit Prince', 'Antoine de Saint-Exupéry', cat_objs[0], 1943, True),
    ('1984', 'George Orwell', cat_objs[1], 1949, True),
    ('Dune', 'Frank Herbert', cat_objs[1], 1965, False),
    ('Sapiens', 'Yuval Noah Harari', cat_objs[2], 2011, True),
    ('Python pour les débutants', 'Eric Matthes', cat_objs[3], 2015, True),
    ('Le Meilleur des Mondes', 'Aldous Huxley', cat_objs[1], 1932, True),
    ('L\'Étranger', 'Albert Camus', cat_objs[4], 1942, False),
    ('Clean Code', 'Robert C. Martin', cat_objs[3], 2008, True),
]

for titre, auteur, cat, annee, dispo in livres:
    Livre.objects.get_or_create(
        titre=titre,
        defaults={'auteur': auteur, 'categorie': cat, 'annee_publication': annee, 'disponible': dispo}
    )
print(f"Données créées : {Categorie.objects.count()} catégories, {Livre.objects.count()} livres")
