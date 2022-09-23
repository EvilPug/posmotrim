from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search_results, name='search'),
    path('film/<int:pk>', views.film_detail, name='film-detail'),
    path('watching/<int:pk>', views.tag_film, name='watching_tag'),
    path('watched/<int:pk>', views.tag_film, name='watched_tag'),
    path('plan/<int:pk>', views.tag_film, name='plan_tag'),
    path('quit/<int:pk>', views.tag_film, name='quit_tag'),

]
