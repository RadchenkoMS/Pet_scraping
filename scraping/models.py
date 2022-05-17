from django.db import models
import datetime
from scraping.utils import from_cyrillic_to_eng


class City(models.Model):
    name = models.CharField(max_length=40, verbose_name='имя города')
    slug = models.CharField(max_length=50, blank=True)

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = from_cyrillic_to_eng(str(self.name))
        super().save(*args, **kwargs)


class Symptom(models.Model):
    name = models.CharField(max_length=40, verbose_name='симптом')
    slug = models.CharField(max_length=50, blank=True)

    class Meta:
        verbose_name = 'Симптом'
        verbose_name_plural = 'Симптомы'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = from_cyrillic_to_eng(str(self.name))
        super().save(*args, **kwargs)


class Application(models.Model):
    url = models.URLField(unique=True)
    title = models.CharField(max_length=200, verbose_name='Запрос')
    credit = models.CharField(max_length=200, verbose_name='Автор')
    timestamp = models.DateField(auto_now_add=True)
    description = models.TextField(
        verbose_name='Описание',
        default='No description ')
    city = models.ForeignKey(
        'City',
        on_delete=models.CASCADE,
        verbose_name='город')
    symptom = models.ForeignKey(
        'Symptom',
        on_delete=models.CASCADE,
        verbose_name='симптом')

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявка'

    def __str__(self):
        return self.title
