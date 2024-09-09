from django.shortcuts import render

from films.models import FilmsModel


def Film_views(request):
    film = FilmsModel.objects.all()

    return render(request, 'films_list.html', {"film":film})

def Film_with_actors_views(request,id):
    film = FilmsModel.objects.all().filter(id=id).first()
    actors = film.actors.all()
    actors_list = []
    for act in actors:
        actors_list.append(act)



    return render(request, 'Film_list_one.html', {"film":film,
                                                                       "actors_list": actors_list })