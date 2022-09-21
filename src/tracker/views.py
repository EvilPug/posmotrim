from django.shortcuts import render
from django.http import JsonResponse

from tracker.models import Film


def home(request):
    return render(request, 'index.html')


def search_results(request):
    if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
        res = None
        film = request.POST.get('film')
        obj = Film.objects.filter(name__icontains=film)
        if len(obj) > 0 and len(film) > 0:
            data = []
            for pos in obj[:4]:
                item = {
                    'pk': pos.pk,
                    'name': pos.name
                }
                data.append(item)
            res = data
        else:
            res = 'Nothing found ...'
        return JsonResponse({'data': res})
    return JsonResponse({})


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
