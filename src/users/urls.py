from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    path('register', views.register_request, name='register'),
    path('login', views.login_request, name='login'),
    path('logout', views.logout_request, name='logout'),
    path('<int:pk>', views.user_detail, name='user-detail'),
    path('friends', views.friends_detail, name='friends-detail'),
    path('search/', views.friends_search, name='friends-search'),
    path('friend-request/<int:pk>', views.friend_request, name='user-detail'),
    path('accept/<int:pk>', views.accept_request, name='accept_request'),
    path('reject/<int:pk>', views.reject_request, name='reject_request')
]
