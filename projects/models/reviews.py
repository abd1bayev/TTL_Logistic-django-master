# models.py
from django.db import models
from django.utils.translation import gettext_lazy as _


class Review(models.Model):
    service = models.ForeignKey(
        'Service',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name="reviews",
        verbose_name=_("Услуга"),
        help_text=_("Укажите услугу, к которой относится этот отзыв.")
    )
    phone_number = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        verbose_name=_("Номер телефона"),
        help_text=_("Введите ваш номер телефона.")
    )
    title = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name=_("Заголовок"),
        help_text=_("Введите заголовок.")
    )
    index_code = models.CharField(
        max_length=20,
        blank=True,
        null=True,
        verbose_name=_("Индекс"),
        help_text=_("Введите индекс.")
    )
    name = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name=_("Имя"),
        help_text=_("Введите ваше имя.")
    )
    surname = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name=_("Фамилия"),
        help_text=_("Введите вашу фамилию.")
    )
    address = models.TextField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name=_("Адрес"),
        help_text=_("Введите ваш адрес.")
    )
    note = models.TextField(
        verbose_name=_("Заметка"),
        blank=True,
        null=True,
        help_text=_("Введите любые дополнительные заметки.")
    )
    description = models.TextField(
        verbose_name=_("Описание"),
        blank=True,
        null=True,
        help_text=_("Напишите описание отзыва о данной услуге.")
    )
    mail = models.EmailField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name=_("Электронная почта"),
        help_text=_("Введите ваш адрес электронной почты.")
    )

    images = models.ManyToManyField(
        'Image',
        blank=True,
        related_name='reviews',
        verbose_name=_("Изображения"),
        help_text=_("Выберите изображения для этого отзыва."),
    )

    class Meta:
        verbose_name = _("Online Application")
        verbose_name_plural = _("Online Application")

    def __str__(self):
        return f"{self.title}: {self.title}"


class Image(models.Model):
    review = models.ForeignKey(
        'Review',
        on_delete=models.CASCADE,
        null=True,
        related_name='review_images',
        verbose_name=_("Отзыв"),
        help_text=_("Отзыв, к которому относится изображение."),
    )

    image = models.ImageField(
        upload_to='review_images',
        verbose_name=_("Изображение"),
        help_text=_("Загрузите изображение.")
    )

    class Meta:
        verbose_name = _("Изображение")
        verbose_name_plural = _("Изображения")

    def __str__(self):
        return self.image.name


# class Review_Image(models.Model):
#     review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='images_review')
#     image = models.ImageField(
#         verbose_name=_("Imagereview"),
#         upload_to='review_images/',
#     )
