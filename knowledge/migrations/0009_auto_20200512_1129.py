# Generated by Django 3.0.5 on 2020-05-12 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('knowledge', '0008_auto_20200511_2159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='content_1',
            field=models.TextField(blank=True, max_length=100, verbose_name='Текст задания'),
        ),
    ]
