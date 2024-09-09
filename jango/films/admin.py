from django.contrib import admin

from films.models import FilmsModel, ActorsModel

admin.site.register(FilmsModel)
admin.site.register(ActorsModel)
