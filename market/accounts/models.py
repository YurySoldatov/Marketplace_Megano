from django.db import models
from django.contrib.auth.models import User


def avatar_image_directory_path(instanse: "Avatar", filename):
    return f"avatars/images/{instanse.profile.pk}/{filename}"


class Avatar(models.Model):
    class Meta:
        verbose_name = "Аватар"
        verbose_name_plural = "Аватары"
        ordering = ["pk"]

    profile = models.OneToOneField("Profile", on_delete=models.CASCADE, verbose_name='Аватар')
    image = models.FileField(upload_to=avatar_image_directory_path, verbose_name="Путь к файлу")


class Profile(models.Model):
    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"
        ordering = ["pk"]

    user = models.OneToOneField(User, on_delete=models.CASCADE, null=False, verbose_name="Пользователь")
    fullName = models.CharField(max_length=256, null=False, blank=True, default='', verbose_name="Полное имя")
    email = models.EmailField(max_length=128, verbose_name="Email")
    phone = models.CharField(max_length=64, verbose_name="Телефон")


