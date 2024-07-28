
from django import forms
from .models import PropTasks,MessageTask

class PropTaskForm(forms.ModelForm):

    class Meta:
        model = PropTasks
        fields = ["title", "user", "desc"]
        widgets = {
            "user": forms.HiddenInput(),
            "title": forms.TextInput(attrs={'placeholder': 'Введите Название'}),
            "desc": forms.Textarea()
        }

class MessageTaskForm(forms.ModelForm):

    class Meta:
        model = MessageTask
        fields = ["message", "user", "task"]
        widgets = {
            'user': forms.HiddenInput(),
            'task': forms.HiddenInput(),
            'message': forms.Textarea(attrs={
                'class': 'chat-input',
                'placeholder': 'Введите сообщение...'
            })
        }