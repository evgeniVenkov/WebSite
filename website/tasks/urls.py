from django.urls import path
from . import views

urlpatterns = [
    path("", views.TasksPage.as_view(), name="tasks"),
    path("<slug>", views.TaskPage.as_view(), name="task"),
    path("PropTask/", views.PropTasksPage.as_view(), name="Prop_Task"),
]
