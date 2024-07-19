from django.shortcuts import redirect
from django.views.generic import ListView, DetailView,CreateView
from .models import Tasks, PropTasks
from.forms import PropTaskForm
from users.models import Message
from users.forms import MessageForm
from django.contrib import messages

class TasksPage(ListView):
    model = Tasks
    template_name = "tasks/tasks_page.html"
    context_object_name = "tasks"
    ordering = ["-id"]

    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super(TasksPage, self).get_context_data(**kwargs)
        ctx["title"] = "Страница с задачами"
        return ctx

class PropTasksPage(CreateView):
    model = PropTasks
    template_name = "tasks/proptasks_page.html"
    form_class = PropTaskForm
    def get_context_data(self, *, object_list=None, **kwargs):
        ctx = super(PropTasksPage, self).get_context_data(**kwargs)
        ctx['title'] = "Предложить задачу"
        return ctx

    def post(self, request, *args, **kwargs):
        post = request.POST.copy()
        post['user'] = request.user
        request.POST = post
        form = PropTaskForm(post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ваше предложение успешно отпрвлено')
        else: print(form.errors)

        return redirect("home")


class TaskPage(DetailView):
    model = Tasks
    template_name = "tasks/taskPage.html"

    def get_context_data(self, *, object_list=None, **kwargs):

        ctx = super(TaskPage, self).get_context_data(**kwargs)

        task = Tasks.objects.filter(slug=self.kwargs['slug']).first()

        ctx["title"] = task.title
        ctx["allmessage"] = Message.objects.filter(task=task)
        ctx['messageform'] = MessageForm
        return ctx

    def post(self, request, *args, **kwargs):
        task = Tasks.objects.filter(slug=self.kwargs['slug']).first()

        post = request.POST.copy()
        post['task'] = task
        post['user'] = request.user
        request.POST = post

        form = MessageForm(post)
        if form.is_valid():
            form.save()

        else:
            print(form.errors)

        return redirect('/tasks/' + self.kwargs['slug'])

