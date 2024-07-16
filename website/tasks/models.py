from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Tasks(models.Model):
    slug = models.SlugField("уникальное название", unique=True)
    title = models.CharField("Название задачи", max_length=100)
    desk = models.TextField("Описание задачи")
    url = models.CharField("ссылка на чат", max_length=130)
    image = models.ImageField(
        "Картинка", default="tasks_Image/default.jpg", upload_to="tasks_Image"
    )

    def __str__(self):
        return self.slug

    def get_absolute_url(self):
        return reverse("task", kwargs={"slug": self.slug})



class PropTasks(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    title = models.CharField("Название задачи", max_length=100)
    desc = models.TextField("Описание задачи")

    def __str__(self):
        return self.title
