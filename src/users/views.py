from django.shortcuts import render, redirect
from .forms import SpectatorCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

from .models import Spectator


def user_detail(request, pk):
    user = Spectator.objects.get(pk=pk)
    req_user = request.user
    user_watched = list(user.films.keys())

    return render(request, 'user_detail.html', context={'user': user})


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
