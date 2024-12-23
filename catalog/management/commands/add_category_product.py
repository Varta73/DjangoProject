from django.core.management.base import BaseCommand
from django.core.management import call_command
from catalog.models import Category, Product


class Command(BaseCommand):
    help = "Добавление категорий и продуктов из фикстур"

    def handle(self, *args, **kwargs):
        # Удаление существующих записей в БД
        Category.objects.all().delete()
        Product.objects.all().delete()

        # Загрузка данных из фикстур
        call_command('loaddata', 'category_fixture')
        call_command('loaddata', 'product_fixture')
        self.stdout.write(self.style.SUCCESS('Данные из фикстуры успешно загружены'))
