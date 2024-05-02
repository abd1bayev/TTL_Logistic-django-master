# Generated by Django 4.2.3 on 2024-05-02 12:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("projects", "0006_alter_review_images"),
    ]

    operations = [
        migrations.AddField(
            model_name="image",
            name="review",
            field=models.ForeignKey(
                help_text="Отзыв, к которому относится изображение.",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="review_images",
                to="projects.review",
                verbose_name="Отзыв",
            ),
        ),
    ]
