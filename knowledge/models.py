from django.db import models
from django.contrib.auth.models import User
# https://github.com/carltongibson/django-filter
# https://github.com/rasca/django-enhanced-cbv

# Create your models here.
class Task(models.Model):
    TASK_TYPES = (('Цепочка', 'Цепочка'), ('Расчетная задача', 'Расчетная задача'))
    LEVELS = ((8, 8), (9, 9), (10, 10), (11, 11))
    author = models.ForeignKey(User, on_delete=models.PROTECT, blank=True, null=True, verbose_name='Автор')
    title = models.CharField(max_length=60, choices=TASK_TYPES, verbose_name='Тип задания')
    content_1 = models.TextField(blank=True, null=False, max_length=700, verbose_name='Текст задания')
    content_2 = models.ImageField(upload_to='task_images', blank=True, null=False, verbose_name='Фото задания')
    level = models.IntegerField(choices=LEVELS, verbose_name='Класс')

    class Meta:
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'
        ordering = ['id']

    def __str__(self):
        if self.content_1 == '':
            return self.title + ' №' + str(self.id)
        else:
            return self.content_1
