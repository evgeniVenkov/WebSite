from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.Tasks_Page.as_view(), name='tasks'),
    path('<slug>',views.TaskPage.as_view(), name='task'),
]