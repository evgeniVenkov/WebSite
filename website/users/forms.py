from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile,Message


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


class MessageForm(forms.ModelForm):

    class Meta:
        model = Message
        fields = ["message","user","task"]
        widgets = {'user': forms.HiddenInput(),
                   'task': forms.HiddenInput(),
                   'message': forms.Textarea(attrs={'placeholder': 'текст сообщения'})}

