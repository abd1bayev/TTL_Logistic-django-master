# Generated by Django 4.2.3 on 2024-04-24 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='description_en',
            field=models.TextField(help_text='Напишите описание отзыва о данной услуге.', null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='review',
            name='description_ru',
            field=models.TextField(help_text='Напишите описание отзыва о данной услуге.', null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='review',
            name='description_uz',
            field=models.TextField(help_text='Напишите описание отзыва о данной услуге.', null=True, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='review',
            name='name_en',
            field=models.CharField(help_text='Введите ваше имя.', max_length=100, null=True, verbose_name='Имя'),
        ),
        migrations.AddField(
            model_name='review',
            name='name_ru',
            field=models.CharField(help_text='Введите ваше имя.', max_length=100, null=True, verbose_name='Имя'),
        ),
        migrations.AddField(
            model_name='review',
            name='name_uz',
            field=models.CharField(help_text='Введите ваше имя.', max_length=100, null=True, verbose_name='Имя'),
        ),
    ]
