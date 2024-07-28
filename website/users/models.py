from django.db import models
from django.contrib.auth.models import User, AbstractUser
from PIL import Image


TYPE_ACCOUNT = (("full", "Полный пакет"), ("free", "Бесплатный пакет"))



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    img = models.ImageField(
        default="user_images/default_us.png", upload_to="user_images"
    )
    account_type = models.CharField(choices=TYPE_ACCOUNT, default="free", max_length=30)

    def __str__(self):
        return f"Профайл пользователя {self.user.username}"

    def save(self, *args, **kwargs):
        super().save()

        image = Image.open(self.img.path)

        if image.height > 256 or image.width > 256:
            resize = (256, 256)
            image.thumbnail(resize)
            image.save(self.img.path)


class messUser(models.Model):
    sender = models.ForeignKey(User, on_delete=models.PROTECT,related_name="sender")
    recipient = models.ForeignKey(User, on_delete=models.PROTECT)
    message = models.TextField()

    def __str__(self):
        return str(self.sender)