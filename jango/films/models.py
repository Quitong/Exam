from django.db import models

class ActorsModel(models.Model):
    name = models.CharField(max_length=100)
    born = models.DateTimeField()

class FilmsModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    release = models.DateTimeField()
    actors = models.ManyToManyField(ActorsModel, null=True)

