from django import forms
from .models import Livre, Categorie


class LivreForm(forms.ModelForm):
    class Meta:
        model = Livre
        fields = ['titre', 'auteur', 'categorie', 'annee_publication', 'description', 'couverture', 'disponible']
        widgets = {
            'titre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Titre du livre'}),
            'auteur': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom de l\'auteur'}),
            'categorie': forms.Select(attrs={'class': 'form-select'}),
            'annee_publication': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '2024'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Brève description...'}),
            'couverture': forms.FileInput(attrs={'class': 'form-control'}),
            'disponible': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }


class CategorieForm(forms.ModelForm):
    class Meta:
        model = Categorie
        fields = ['nom']
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom de la catégorie'}),
        }
