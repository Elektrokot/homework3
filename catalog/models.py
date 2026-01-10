from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Наименование")
    description = models.TextField(verbose_name="Описание")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name']


class Product(models.Model):
    title = models.CharField(max_length=100, verbose_name="Наименование")
    description = models.TextField(verbose_name="Описание")
    image = models.ImageField(upload_to='products/', verbose_name="Изображение", blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категория")
    price = models.FloatField(verbose_name="Цена за покупку")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата последнего изменения")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['title']


class Contact(models.Model):
    address = models.CharField(max_length=200, verbose_name="Адрес")
    phone = models.CharField(max_length=20, verbose_name="Телефон")
    email = models.EmailField(verbose_name="Email")
    working_hours = models.CharField(max_length=100, verbose_name="Время работы")

    def __str__(self):
        return f"Контакт: {self.address}"

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"
