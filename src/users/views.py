from django.shortcuts import render, redirect
from .forms import SpectatorCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

from .models import Spectator
from tracker.models import Film


def user_detail(request, pk):
    login_user = request.user
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

    return render(request, 'user_detail.html', context={'user': user,
                                                        'login_user': login_user,
                                                        'watched': watched,
                                                        'watching': watching,
                                                        'plan': plan,
                                                        'quit': quit})


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
