# Generated by Django 4.2.3 on 2024-05-26 18:14

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("projects", "0002_remove_blog_view_count"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="blog",
            name="address",
        ),
        migrations.RemoveField(
            model_name="blog",
            name="address_en",
        ),
        migrations.RemoveField(
            model_name="blog",
            name="address_ru",
        ),
        migrations.RemoveField(
            model_name="blog",
            name="address_uz",
        ),
        migrations.RemoveField(
            model_name="blog",
            name="country",
        ),
        migrations.RemoveField(
            model_name="blog",
            name="country_en",
        ),
        migrations.RemoveField(
            model_name="blog",
            name="country_ru",
        ),
        migrations.RemoveField(
            model_name="blog",
            name="country_uz",
        ),
    ]
