# Generated by Django 4.2.3 on 2024-05-02 08:12

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("projects", "0002_review_description_en_review_description_ru_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="review_image",
            name="review",
        ),
        migrations.DeleteModel(
            name="Review",
        ),
        migrations.DeleteModel(
            name="Review_Image",
        ),
    ]