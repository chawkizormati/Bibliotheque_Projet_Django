from django.contrib import admin
from .models import Livre, Categorie

@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display = ['nom']
    search_fields = ['nom']

@admin.register(Livre)
class LivreAdmin(admin.ModelAdmin):
    list_display = ['titre', 'auteur', 'categorie', 'annee_publication', 'disponible']
    list_filter = ['disponible', 'categorie']
    search_fields = ['titre', 'auteur']
