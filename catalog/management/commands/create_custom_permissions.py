from django.core.management.base import BaseCommand
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from catalog.models import Product

class Command(BaseCommand):
    help = 'Создаёт кастомное право "can_unpublish_product"'

    def handle(self, *args, **options):
        content_type = ContentType.objects.get_for_model(Product)  # Получаем ContentType для модели Product

        perm, created = Permission.objects.get_or_create(  # Получаем кастомное право
            codename='can_unpublish_product',
            name='Can unpublish product',
            content_type=content_type,)

        if created:                                         # Проверка на создание права.
            self.stdout.write(self.style.SUCCESS('Право "can_unpublish_product" успешно создано.'))
        else:
            self.stdout.write(self.style.WARNING('Право "can_unpublish_product" уже существует.'))
