from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Livre, Categorie
from .forms import LivreForm, CategorieForm


def accueil(request):
    total_livres = Livre.objects.count()
    livres_disponibles = Livre.objects.filter(disponible=True).count()
    total_categories = Categorie.objects.count()
    derniers_livres = Livre.objects.all()[:4]
    context = {
        'total_livres': total_livres,
        'livres_disponibles': livres_disponibles,
        'total_categories': total_categories,
        'derniers_livres': derniers_livres,
    }
    return render(request, 'livres/accueil.html', context)


@login_required
def liste_livres(request):
    query = request.GET.get('q', '')
    categorie_id = request.GET.get('categorie', '')
    livres = Livre.objects.select_related('categorie').all()

    if query:
        livres = livres.filter(
            Q(titre__icontains=query) |
            Q(auteur__icontains=query) |
            Q(description__icontains=query)
        )
    if categorie_id:
        livres = livres.filter(categorie_id=categorie_id)

    paginator = Paginator(livres, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    categories = Categorie.objects.all()
    context = {
        'page_obj': page_obj,
        'query': query,
        'categories': categories,
        'categorie_id': categorie_id,
    }
    return render(request, 'livres/liste_livres.html', context)


@login_required
def detail_livre(request, pk):
    livre = get_object_or_404(Livre, pk=pk)
    return render(request, 'livres/detail_livre.html', {'livre': livre})


@login_required
def ajouter_livre(request):
    if request.method == 'POST':
        form = LivreForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Livre ajouté avec succès !')
            return redirect('liste_livres')
    else:
        form = LivreForm()
    return render(request, 'livres/form_livre.html', {'form': form, 'action': 'Ajouter'})


@login_required
def modifier_livre(request, pk):
    livre = get_object_or_404(Livre, pk=pk)
    if request.method == 'POST':
        form = LivreForm(request.POST, request.FILES, instance=livre)
        if form.is_valid():
            form.save()
            messages.success(request, 'Livre modifié avec succès !')
            return redirect('liste_livres')
    else:
        form = LivreForm(instance=livre)
    return render(request, 'livres/form_livre.html', {'form': form, 'action': 'Modifier', 'livre': livre})


@login_required
def supprimer_livre(request, pk):
    livre = get_object_or_404(Livre, pk=pk)
    if request.method == 'POST':
        livre.delete()
        messages.success(request, 'Livre supprimé avec succès !')
        return redirect('liste_livres')
    return render(request, 'livres/confirmer_suppression.html', {'livre': livre})



@login_required
def liste_categories(request):
    categories = Categorie.objects.all()
    return render(request, 'livres/liste_categories.html', {'categories': categories})


@login_required
def ajouter_categorie(request):
    if request.method == 'POST':
        form = CategorieForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Catégorie ajoutée !')
            return redirect('liste_categories')
    else:
        form = CategorieForm()
    return render(request, 'livres/form_categorie.html', {'form': form, 'action': 'Ajouter'})


@login_required
def modifier_categorie(request, pk):
    categorie = get_object_or_404(Categorie, pk=pk)
    if request.method == 'POST':
        form = CategorieForm(request.POST, instance=categorie)
        if form.is_valid():
            form.save()
            messages.success(request, 'Catégorie modifiée !')
            return redirect('liste_categories')
    else:
        form = CategorieForm(instance=categorie)
    return render(request, 'livres/form_categorie.html', {'form': form, 'action': 'Modifier'})


@login_required
def supprimer_categorie(request, pk):
    categorie = get_object_or_404(Categorie, pk=pk)
    if request.method == 'POST':
        categorie.delete()
        messages.success(request, 'Catégorie supprimée !')
        return redirect('liste_categories')
    return render(request, 'livres/confirmer_suppression_categorie.html', {'categorie': categorie})
