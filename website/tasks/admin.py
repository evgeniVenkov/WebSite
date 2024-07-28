from django.contrib import admin
from .models import Tasks,PropTasks,MessageTask

admin.site.register(PropTasks)
admin.site.register(Tasks)
admin.site.register(MessageTask)
