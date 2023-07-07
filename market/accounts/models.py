from django.db import models
from django.contrib.auth.models import User


def avatar_image_directory_path(instance: "Avatar", filename):
    return f"avatars/images/{instance.profile.pk}/{filename}"


class Avatar(models.Model):
    class Meta:
        verbose_name = "Аватар"
        verbose_name_plural = "Аватары"
        ordering = ["pk"]

    profile = models.OneToOneField("Profile", on_delete=models.CASCADE, verbose_name='Аватар')
    image = models.FileField(upload_to=avatar_image_directory_path, verbose_name="Путь к файлу")

    def src(self):
        return f"/media/{self.image}"

    def alt(self):
        return f"{self.profile.user.username}_avatar"

    def __str__(self):
        return f"{self.profile.user.username}_avatar"


class Profile(models.Model):
    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"
        ordering = ["pk"]

    user = models.OneToOneField(User, on_delete=models.CASCADE, null=False, verbose_name="Пользователь")
    fullName = models.CharField(max_length=256, null=False, blank=True, default='', verbose_name="Полное имя")
    email = models.EmailField(max_length=128, verbose_name="Email")
    phone = models.CharField(max_length=64, verbose_name="Телефон")

    def __str__(self):
        return f"{self.user.username}_profile"
