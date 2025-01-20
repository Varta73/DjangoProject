from django.db import models


class Blog(models.Model):
    objects = None
    title = models.CharField(max_length=200, verbose_name='Заголовок блога')
    content = models.TextField(null=True, verbose_name='Содержание')
    image = models.ImageField(upload_to='images/', blank=True, null=True, verbose_name='Изображение')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    is_published = models.BooleanField(verbose_name='Опубликовано')
    views_counter = models.PositiveIntegerField(verbose_name='Количество просмотров', default=0)

    def __str__(self):
        return f'{self.title} '

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'
