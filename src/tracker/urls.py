from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('film/<int:pk>', views.film_detail, name='film-detail'),
]
