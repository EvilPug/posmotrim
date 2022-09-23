from django.shortcuts import render, redirect
from django.http import JsonResponse

from tracker.models import Film
from users.models import Spectator


def home(request):
    comedy = Film.objects.filter(genres__icontains="комедия").order_by('-rating_imdb')[:3]
    drama = Film.objects.filter(genres__icontains="драма").order_by('-rating_imdb')[:3]
    return render(request, 'index.html', context={'comedy': comedy,
                                                  'drama': drama})


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
    close_films = Film.objects.filter(pk__in=film.close)
    user = request.user

    if user.is_anonymous:
        stats = {'rated': 'Вы не авторизованы',
                 'status': 'Вы не авторизованы'}
    else:
        user_watched = list(user.films.keys())

        if str(film.pk) in user_watched:
            stats = user.films[str(film.pk)]
        else:
            stats = {'rated': None, 'status': None}

    return render(request, 'film_detail.html', context={'film': film,
                                                        'stats': stats,
                                                        'close_films': close_films})


def film_rate(request, pk):
    return render(request, 'film_detail.html')


def tag_film(request, pk):
    new_status = request.path.split('/')[1]
    if request.user.is_authenticated:
        user = Spectator.objects.get(pk=request.user.pk)
        user_films = list(user.films.keys())
        if str(pk) in user_films:
            user.films.get(str(pk))['status'] = new_status
            user.save()
        else:
            user.films.update({str(pk): {
                                                "rated": 0,
                                                "status": new_status}})
            user.save()

        return redirect('/film/' + str(pk))
