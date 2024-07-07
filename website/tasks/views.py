from django.shortcuts import render
from django.views.generic import ListView

from .models import Tasks


class Tasks_Page(ListView):
    model = Tasks
    template_name = 'tasks/tasks_page.html'
    context_object_name = 'tasks'
    ordering = ['-id']

    def get_context_data(self,*,object_list=None, **kwargs):
        ctx = super(Tasks_Page, self).get_context_data(**kwargs)
        ctx['title'] = 'Страница с задачами'
        return ctx