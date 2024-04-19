from projects.utils import BaseModel
from django.db import models
from .service import Service


class Review(BaseModel):
    service = models.ForeignKey(
        Service,
        on_delete=models.CASCADE,
        related_name="reviews",
        verbose_name="Услуга",
        help_text="Укажите услугу, к которой относится этот отзыв."
    )
    full_name = models.CharField(
        max_length=50,
        verbose_name="Полное имя",
        help_text="Укажите ваше полное имя."
    )
    description = models.TextField(
        verbose_name="Описание",
        help_text="Напишите описание отзыва о данной услуге."
    )
    file = models.FileField(blank=True, null=True, upload_to='files/')
    is_active = models.BooleanField(
        default=False,
        verbose_name="Активен",
        help_text="Установите значение 'True', чтобы активировать этот отзыв."
    )

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"

    def __str__(self):
        return f"{self.service}: {self.full_name}"
