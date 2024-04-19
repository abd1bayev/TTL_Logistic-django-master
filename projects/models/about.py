from django.db import models
from django.utils.translation import gettext_lazy as _


class About(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name="Заголовок",
        help_text="Введите заголовок для объекта."
    )

    content = models.TextField(
        verbose_name="Содержание",
        help_text="Введите содержание для объекта."
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания",
        help_text="Дата и время создания объекта будут автоматически заполнены."
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата обновления",
        help_text="Дата и время обновления объекта будут автоматически обновляться при сохранении."
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("О нас")
        verbose_name_plural = _("О нас (множественное число)")
