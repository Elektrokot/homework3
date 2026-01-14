from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from blog.models import BlogPost


class Command(BaseCommand):
    help = 'Создаёт группу "Контент-менеджер" с правами на управление блогом'

    def handle(self, *args, **options):
        group, created = Group.objects.get_or_create(name='Контент-менеджер')  # Создаём группу контент-менеджеров

        content_type = ContentType.objects.get_for_model(BlogPost)


        change_post_perm = Permission.objects.get(codename='change_blogpost', content_type=content_type)  # получаем права
        delete_post_perm = Permission.objects.get(codename='delete_blogpost', content_type=content_type)

        group.permissions.add(change_post_perm, delete_post_perm)  # Присваиваем права группе

        if created:                                                                         # Проверка создания группы.
            self.stdout.write(self.style.SUCCESS('Группа "Контент-менеджер" успешно создана и права назначены.'))
        else:
            self.stdout.write(self.style.WARNING('Группа "Контент-менеджер" уже существует, права обновлены.'))
