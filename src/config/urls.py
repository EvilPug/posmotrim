from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('tracker.urls')),
    path('users/', include('users.urls')),
    path('admin/', admin.site.urls),
    path('friendship/', include('friendship.urls')),
]
