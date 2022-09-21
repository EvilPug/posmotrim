from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import SpectatorCreationForm, SpectatorChangeForm
from .models import Spectator


class SpectatorAdmin(UserAdmin):
    add_form = SpectatorCreationForm
    form = SpectatorChangeForm
    model = Spectator
    list_display = ['email', 'username', ]


admin.site.register(Spectator, SpectatorAdmin)
