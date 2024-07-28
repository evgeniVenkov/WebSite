from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile,messUser


class MessUserForm(forms.ModelForm):
    class Meta:
        model = messUser
        fields = "__all__"
        widgets = {
            "sender":forms.HiddenInput(),
            "recipient": forms.HiddenInput(),
            "message": forms.Textarea(attrs={
                'class': 'chat-input',
                'placeholder': 'Введите сообщение...'
            })
        }
class UserOurRegistraion(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "password1", "password2", "email"]


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email"]


class ProfileImage(forms.ModelForm):
    def __init__(self, *args, **kwards):
        super(ProfileImage, self).__init__(*args, **kwards)
        self.fields["img"].label = "Изображение профиля"

    class Meta:
        model = Profile
        fields = ["img"]



