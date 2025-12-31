from django.core.management.base import BaseCommand
from django.core.management import call_command

class Command(BaseCommand):
    help = 'Удаляет все данные из базы и заполняет её тестовыми данными из фикстур'

    def handle(self, *args, **options):
        self.stdout.write("Удаление всех данных из базы...")
        # Удаляем все данные
        call_command('flush', verbosity=0, interactive=False)

        self.stdout.write("Загрузка тестовых данных из фикстуры...")
        # Загружаем фикстуру
        call_command('loaddata', 'catalog_fixture.json', verbosity=1)

        self.stdout.write(
            self.style.SUCCESS('База данных успешно заполнена тестовыми данными!')
        )
