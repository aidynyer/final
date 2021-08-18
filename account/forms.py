from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from account.models import User


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'profile_picture', 'first_name', 'last_name', 'phone', 'password1', 'password2']


class UpdateUserForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'phone', 'about_me', 'profile_picture']
