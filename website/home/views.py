from django.shortcuts import render
from django.views.generic import ListView

from . models import Post


class home_Page(ListView):
    model = Post
    template_name = 'home/home.html'
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
        ctx = super(home_Page, self).get_context_data(**kwargs)
        ctx['title'] = "Домашняя страница"
        return ctx