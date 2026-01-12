from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True, verbose_name="Электронная почта")
    avatar = models.ImageField(upload_to='avatars/', verbose_name="Аватар", blank=True, null=True)
    phone_number = models.CharField(max_length=15, verbose_name="Номер телефона", blank=True, null=True)
    country = models.CharField(max_length=50, verbose_name="Страна", blank=True, null=True)

    USERNAME_FIELD = 'email'  # Используем email вместо username
    REQUIRED_FIELDS = ['username']  # username остаётся обязательным для суперпользователя

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"
