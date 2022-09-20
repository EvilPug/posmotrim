from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from users.models import Spectator


class SpectatorCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = Spectator
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(SpectatorCreationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class SpectatorChangeForm(UserChangeForm):

    class Meta:
        model = Spectator
        fields = ("username", "email")
