
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100, verbose_name='Nom de la catégorie')),
            ],
            options={
                'verbose_name': 'Catégorie',
                'ordering': ['nom'],
            },
        ),
        migrations.CreateModel(
            name='Livre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=200, verbose_name='Titre')),
                ('auteur', models.CharField(max_length=150, verbose_name='Auteur')),
                ('annee_publication', models.PositiveIntegerField(verbose_name='Année de publication')),
                ('description', models.TextField(blank=True, verbose_name='Description')),
                ('couverture', models.ImageField(blank=True, null=True, upload_to='couvertures/', verbose_name='Image de couverture')),
                ('disponible', models.BooleanField(default=True, verbose_name='Disponible')),
                ('date_ajout', models.DateTimeField(auto_now_add=True)),
                ('categorie', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='livres', to='livres.categorie', verbose_name='Catégorie')),
            ],
            options={
                'verbose_name': 'Livre',
                'ordering': ['-date_ajout'],
            },
        ),
    ]
