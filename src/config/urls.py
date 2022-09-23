from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('tracker.urls', namespace="tracker")),
    path('users/', include('users.urls', namespace="users")),
    path('admin/', admin.site.urls),
    path('friendship/', include('friendship.urls')),
]
