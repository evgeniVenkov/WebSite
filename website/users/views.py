from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserOurRegistraion, ProfileImage, UserUpdateForm,MessUserForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import messUser

class UserDetailView(DetailView):
    model = User
    slug_field = 'username'
    slug_url_kwarg = 'username'
    template_name = 'users/alien_user_page.html'

    def get_context_data(self, **kwargs):
        ctx = super(UserDetailView, self).get_context_data(**kwargs)
        sender = User.objects.get(username=self.request.user.username)
        recipient  = User.objects.get(username=self.kwargs['username'])
        ctx['title'] = f'страница пользователя {self.kwargs['username']}'
        ctx['MessageUserForm'] = MessUserForm
        mess = messUser.objects.filter(
            Q(sender = sender,recipient = recipient) | Q(recipient = sender,sender = recipient)

        )
        ctx['MessageUser'] = mess.order_by('id')
        return ctx
    def post(self, request, *args, **kwargs):
        post = request.POST.copy()
        sender = User.objects.get(username=self.request.user.username)
        recipient = User.objects.get(username=self.kwargs['username'])
        post['sender'] = sender
        post['recipient'] = recipient
        request.POST = post

        form = MessUserForm(post)
        if form.is_valid():
            form.save()

        return redirect('/users/' + self.kwargs['username'])

class AllUsers(ListView):
    model = User
    template_name = "users/allUsers.html"
    context_object_name = "users"
    ordering = ['id']

    def get_context_data(self, **kwargs):
        ctx = super(AllUsers, self).get_context_data(**kwargs)
        ctx['title'] = "Все пользователи"
        return ctx

def register(request):
    if request.method == "POST":
        form = UserOurRegistraion(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(
                request,
                f"Аккаунт {username} был создан, введите имя пользователя и пароль для авторизации",
            )
            return redirect("user")
    else:
        form = UserOurRegistraion()
    return render(
        request,
        "users/registration.html",
        {"form": form, "title": "Регистрация пользователя"},
    )

@login_required
def profile(request):
    if request.method == "POST":
        img_profile = ProfileImage(
            request.POST, request.FILES, instance=request.user.profile
        )
        update_user = UserUpdateForm(request.POST, instance=request.user)

        if update_user.is_valid() and img_profile.is_valid():
            update_user.save()
            img_profile.save()
            messages.success(request, f"Ваш аккаунт был успешно обновлен")
            return redirect("profile")
    else:
        img_profile = ProfileImage(instance=request.user.profile)
        update_user = UserUpdateForm(instance=request.user)

    data = {"img_profile": img_profile, "update_user": update_user}

    return render(request, "users/profile.html", data)
