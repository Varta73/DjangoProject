from django.db import models

from django.utils import timezone

from users.models import User


class Category(models.Model):
    objects = None
    name = models.CharField(
        max_length=100,
        verbose_name="Наименование категории",
        help_text="Введите наименование категории",
    )
    description = models.TextField(
        verbose_name="Описание категории",
        help_text="Введите описание категории",
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["name"]


class Product(models.Model):
    objects = None
    name = models.CharField(
        max_length=150,
        verbose_name="Наименование",
    )
    description = models.TextField(
        verbose_name="Описание",
        blank=True,
        null=True,
    )
    image = models.ImageField(
        upload_to="static/images",
        verbose_name="Изображение",
        help_text="Загрузите фото продукта",
        blank=True,
        null=True,
    )
    price = models.IntegerField(verbose_name="Цена")
    created_at = models.DateField(blank=True, null=True, verbose_name="Дата создания", default=timezone.now)
    updated_at = models.DateField(blank=True, null=True, verbose_name="Дата последнего изменения", default=timezone.now)
    status_publication = models.BooleanField(verbose_name="Статус публикации", default=False)
    category = models.ForeignKey(
        Category, verbose_name="Категория", on_delete=models.CASCADE, related_name="category"
    )
    owner = models.ForeignKey(User, verbose_name="Владелец", blank=True, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["name", "price", "created_at", "category"]
        permissions = [
            ('can_unpublish_product', 'Can unpublish product'),

        ]
