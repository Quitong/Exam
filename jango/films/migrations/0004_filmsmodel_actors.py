# Generated by Django 5.1.1 on 2024-09-09 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0003_remove_filmsmodel_actors'),
    ]

    operations = [
        migrations.AddField(
            model_name='filmsmodel',
            name='actors',
            field=models.ManyToManyField(null=True, to='films.actorsmodel'),
        ),
    ]
