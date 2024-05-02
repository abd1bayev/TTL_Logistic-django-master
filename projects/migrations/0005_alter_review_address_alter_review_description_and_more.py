# Generated by Django 4.2.3 on 2024-05-02 09:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("projects", "0004_image_review"),
    ]

    operations = [
        migrations.AlterField(
            model_name="review",
            name="address",
            field=models.TextField(
                blank=True,
                help_text="Введите ваш адрес.",
                max_length=255,
                null=True,
                verbose_name="Адрес",
            ),
        ),
        migrations.AlterField(
            model_name="review",
            name="description",
            field=models.TextField(
                blank=True,
                help_text="Напишите описание отзыва о данной услуге.",
                null=True,
                verbose_name="Описание",
            ),
        ),
        migrations.AlterField(
            model_name="review",
            name="description_en",
            field=models.TextField(
                blank=True,
                help_text="Напишите описание отзыва о данной услуге.",
                null=True,
                verbose_name="Описание",
            ),
        ),
        migrations.AlterField(
            model_name="review",
            name="description_ru",
            field=models.TextField(
                blank=True,
                help_text="Напишите описание отзыва о данной услуге.",
                null=True,
                verbose_name="Описание",
            ),
        ),
        migrations.AlterField(
            model_name="review",
            name="description_uz",
            field=models.TextField(
                blank=True,
                help_text="Напишите описание отзыва о данной услуге.",
                null=True,
                verbose_name="Описание",
            ),
        ),
        migrations.AlterField(
            model_name="review",
            name="images",
            field=models.ManyToManyField(
                blank=True,
                help_text="Выберите изображения для этого отзыва.",
                null=True,
                related_name="reviews",
                to="projects.image",
                verbose_name="Изображения",
            ),
        ),
        migrations.AlterField(
            model_name="review",
            name="index_code",
            field=models.CharField(
                blank=True,
                help_text="Введите индекс.",
                max_length=20,
                null=True,
                verbose_name="Индекс",
            ),
        ),
        migrations.AlterField(
            model_name="review",
            name="mail",
            field=models.EmailField(
                blank=True,
                help_text="Введите ваш адрес электронной почты.",
                max_length=255,
                null=True,
                verbose_name="Электронная почта",
            ),
        ),
        migrations.AlterField(
            model_name="review",
            name="name",
            field=models.CharField(
                blank=True,
                help_text="Введите ваше имя.",
                max_length=100,
                null=True,
                verbose_name="Имя",
            ),
        ),
        migrations.AlterField(
            model_name="review",
            name="name_en",
            field=models.CharField(
                blank=True,
                help_text="Введите ваше имя.",
                max_length=100,
                null=True,
                verbose_name="Имя",
            ),
        ),
        migrations.AlterField(
            model_name="review",
            name="name_ru",
            field=models.CharField(
                blank=True,
                help_text="Введите ваше имя.",
                max_length=100,
                null=True,
                verbose_name="Имя",
            ),
        ),
        migrations.AlterField(
            model_name="review",
            name="name_uz",
            field=models.CharField(
                blank=True,
                help_text="Введите ваше имя.",
                max_length=100,
                null=True,
                verbose_name="Имя",
            ),
        ),
        migrations.AlterField(
            model_name="review",
            name="note",
            field=models.TextField(
                blank=True,
                help_text="Введите любые дополнительные заметки.",
                null=True,
                verbose_name="Заметка",
            ),
        ),
        migrations.AlterField(
            model_name="review",
            name="phone_number",
            field=models.CharField(
                blank=True,
                help_text="Введите ваш номер телефона.",
                max_length=20,
                null=True,
                verbose_name="Номер телефона",
            ),
        ),
        migrations.AlterField(
            model_name="review",
            name="service",
            field=models.ForeignKey(
                blank=True,
                help_text="Укажите услугу, к которой относится этот отзыв.",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="reviews",
                to="projects.service",
                verbose_name="Услуга",
            ),
        ),
        migrations.AlterField(
            model_name="review",
            name="surname",
            field=models.CharField(
                blank=True,
                help_text="Введите вашу фамилию.",
                max_length=100,
                null=True,
                verbose_name="Фамилия",
            ),
        ),
        migrations.AlterField(
            model_name="review",
            name="title",
            field=models.CharField(
                blank=True,
                help_text="Введите заголовок.",
                max_length=255,
                null=True,
                verbose_name="Заголовок",
            ),
        ),
    ]