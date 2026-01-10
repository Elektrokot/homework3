from django.db import models

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Содержимое")
    preview = models.ImageField(upload_to='blog_previews/', verbose_name="Превью", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    published = models.BooleanField(default=True, verbose_name="Опубликовано")
    views_count = models.PositiveIntegerField(default=0, verbose_name="Количество просмотров")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Запись"
        verbose_name_plural = "Записи"
        ordering = ['-created_at']