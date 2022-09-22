from django.shortcuts import render, redirect
from .forms import SpectatorCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.http import JsonResponse

from .models import Spectator
from tracker.models import Film
from friendship.models import Friend, FriendshipRequest


def user_detail(request, pk):
    user = Spectator.objects.get(pk=pk)
    req_user = request.user
    films = list(user.films.keys())
    watched, watching, plan, quit = [], [], [], []
    for film in films:
        stats = user.films.get(film)
        if stats['status'] == 'watched':
            watched.append({'pk': film,
                            'name': Film.objects.get(pk=films[0]).name})
        elif stats['status'] == 'watching':
            watching.append({'pk': film,
                            'name': Film.objects.get(pk=films[0]).name})
        elif stats['status'] == 'plan':
            plan.append({'pk': film,
                            'name': Film.objects.get(pk=films[0]).name})
        elif stats['status'] == 'quit':
            quit.append({'pk': film,
                            'name': Film.objects.get(pk=films[0]).name})

    rqs = Friend.objects.sent_requests(user=request.user)
    print(rqs)

    return render(request, 'user_detail.html', context={'user': user,
                                                        'watched': watched,
                                                        'watching': watching,
                                                        'plan': plan,
                                                        'quit': quit,
                                                        'rqs': rqs})


def friends_detail(request):
    friends = Friend.objects.friends(request.user)
    requests = Friend.objects.unrejected_requests(user=request.user)
    return render(request, 'friends.html', context={'friends': friends,
                                                    'requests': requests})


def friends_search(request):
    if request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
        res = None
        search_user = request.POST.get('username')
        obj = Spectator.objects.filter(username__icontains=search_user)
        if len(obj) > 0 and len(search_user) > 0:
            data = []
            for pos in obj[:4]:
                item = {
                    'pk': pos.pk,
                    'name': pos.username
                }
                data.append(item)
            res = data
        else:
            res = 'Nothing found ...'
        return JsonResponse({'data': res})
    return JsonResponse({})


def friend_request(request, pk):
    other_user = Spectator.objects.get(pk=pk)
    Friend.objects.add_friend(
        request.user,
        other_user,
        message="Привет! Будь моим семпаем!")
    return user_detail(request, pk)


def accept_request(request, pk):
    other_user = Spectator.objects.get(pk=pk)
    friend_request = FriendshipRequest.objects.get(from_user=other_user, to_user=request.user)
    friend_request.accept()
    return friends_detail(request)


def reject_request(request, pk):
    other_user = Spectator.objects.get(pk=pk)
    friend_request = FriendshipRequest.objects.get(from_user=other_user, to_user=request.user)
    friend_request.reject()
    return friends_detail(request)


def register_request(request):
    if request.method == "POST":
        form = SpectatorCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Регистрация успешна.")
            return redirect("home")
        messages.error(request, "Неверно введены данные.")
    form = SpectatorCreationForm()
    return render(request=request, template_name="register.html",
                  context={"register_form": form})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"Вы авторизованы как {username}.")
                return redirect("home")
            else:
                messages.error(
                    request, "Неправильное имя пользователя или пароль.")
        else:
            messages.error(
                request, "Неправильное имя пользователя или пароль.")
    form = AuthenticationForm()
    return render(request=request, template_name="login.html", context={"login_form": form})


def logout_request(request):
    logout(request)
    messages.info(request, "Вы вышли из аккаунта.")
    return redirect("home")
