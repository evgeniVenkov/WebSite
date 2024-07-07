from django.urls import path,include
from .import views

urlpatterns = [
    path('', views.home_Page.as_view(), name='home'),
]