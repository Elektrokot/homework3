from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission


class Command(BaseCommand):
    help = 'Создаёт группу "Модератор продуктов" с правами на редактирование и снятие с публикации'

    def handle(self, *args, **options):
        group, created = Group.objects.get_or_create(name='Модератор продуктов') # Создаём группу модератор продуктов

        unpublish_perm = Permission.objects.get(codename='can_unpublish_product') # получаем права
        delete_perm = Permission.objects.get(codename='delete_product')

        group.permissions.add(unpublish_perm, delete_perm) # Присваиваем права группе

        if created:  # Проверка создания группы.
            self.stdout.write(self.style.SUCCESS('Группа "Модератор продуктов" успешно создана.'))
        else:
            self.stdout.write(self.style.WARNING('Группа "Модератор продуктов" уже существует.'))
