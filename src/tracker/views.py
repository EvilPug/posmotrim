from django.shortcuts import render

from tracker.models import Film


def home(request):
    return render(request, 'base.html')


def film_detail(request, pk):
    film = Film.objects.get(pk=pk)
    user = request.user
    user_watched = list(user.films.keys())

    if str(film.pk) in user_watched:
        stats = user.films[str(film.pk)]
    else:
        stats = {'rated': 'не оценен', 'status': 'нет статуса'}

    return render(request, 'film_detail.html', context={'film': film,
                                                        'stats': stats})
