# Generated by Django 3.0.5 on 2020-05-10 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('knowledge', '0005_auto_20200506_2224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='level',
            field=models.IntegerField(choices=[(8, 8), (9, 9), (10, 10), (11, 11)], verbose_name='Класс'),
        ),
        migrations.AlterField(
            model_name='task',
            name='title',
            field=models.CharField(choices=[('Цепочка', 'Цепочка'), ('Расчетная задача', 'Расчетная задача')], max_length=60, verbose_name='Тип задания'),
        ),
    ]
