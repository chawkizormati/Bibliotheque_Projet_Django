from django.db import models


class Categorie(models.Model):
    nom = models.CharField(max_length=100, verbose_name="Nom de la catégorie")

    class Meta:
        verbose_name = "Catégorie"
        ordering = ['nom']

    def __str__(self):
        return self.nom


class Livre(models.Model):
    titre = models.CharField(max_length=200, verbose_name="Titre")
    auteur = models.CharField(max_length=150, verbose_name="Auteur")
    categorie = models.ForeignKey(
        Categorie,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='livres',
        verbose_name="Catégorie"
    )
    annee_publication = models.PositiveIntegerField(verbose_name="Année de publication")
    description = models.TextField(blank=True, verbose_name="Description")
    couverture = models.ImageField(
        upload_to='couvertures/',
        null=True,
        blank=True,
        verbose_name="Image de couverture"
    )
    disponible = models.BooleanField(default=True, verbose_name="Disponible")
    date_ajout = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Livre"
        ordering = ['-date_ajout']

    def __str__(self):
        return f"{self.titre} — {self.auteur}"
