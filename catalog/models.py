from django.db import models

from django.utils import timezone


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
        help_text="Введите наименование продукта",
    )
    description = models.TextField(
        verbose_name="Описание",
        help_text="Введите описание продукта",
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
    category = models.ForeignKey(
        Category, verbose_name="Категория", on_delete=models.CASCADE, related_name="products"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["name", "price", "created_at", "category"]
