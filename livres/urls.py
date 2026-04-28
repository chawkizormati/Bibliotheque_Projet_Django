from django.urls import path
from . import views

urlpatterns = [
    # Accueil
    path('', views.accueil, name='accueil'),

    # Livres CRUD
    path('livres/', views.liste_livres, name='liste_livres'),
    path('livres/<int:pk>/', views.detail_livre, name='detail_livre'),
    path('livres/ajouter/', views.ajouter_livre, name='ajouter_livre'),
    path('livres/<int:pk>/modifier/', views.modifier_livre, name='modifier_livre'),
    path('livres/<int:pk>/supprimer/', views.supprimer_livre, name='supprimer_livre'),

    # Catégories CRUD
    path('categories/', views.liste_categories, name='liste_categories'),
    path('categories/ajouter/', views.ajouter_categorie, name='ajouter_categorie'),
    path('categories/<int:pk>/modifier/', views.modifier_categorie, name='modifier_categorie'),
    path('categories/<int:pk>/supprimer/', views.supprimer_categorie, name='supprimer_categorie'),
]
