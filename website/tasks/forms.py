
from django import forms
from .models import PropTasks

class PropTaskForm(forms.ModelForm):

    class Meta:
        model = PropTasks
        fields = ["title", "user", "desc"]
        widgets = {
            "user": forms.HiddenInput(),
            "title": forms.TextInput(attrs={'placeholder': 'Введите Название'}),
            "desc": forms.Textarea()
        }