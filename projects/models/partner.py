from django.db import models
from django.utils.translation import gettext_lazy as _

from projects.utils import BaseModel


class Partner(BaseModel):
    title = models.CharField(
        max_length=100,
        verbose_name=_("Название партнера"),
        help_text=_("Введите название партнера"),
    )

    image = models.ImageField(
        upload_to='partners/',
        blank=True,
        null=True,
        verbose_name=_("Изображение партнера"),
        help_text=_("Загрузите изображение для партнера (необязательно)"),
    )

    url = models.URLField(
        verbose_name=_("URL партнера"),
        help_text=_("Введите URL-адрес партнера"),
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _("Партнер")
        verbose_name_plural = _("Партнеры")
