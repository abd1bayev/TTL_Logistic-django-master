from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

from projects.utils import BaseModel


class Service(BaseModel):
    title = models.CharField(
        max_length=200,
        verbose_name=_("Заголовок"),
        help_text=_("Заголовок услуги")
    )

    slug = models.SlugField(
        max_length=200,
        unique=True,
        blank=True,
        verbose_name=_("URL-часть"),
        help_text=_("URL-часть для заголовка. Автоматически генерируется.")
    )

    image = models.ImageField(
        upload_to='service_images/',
        blank=True,
        null=True,
        verbose_name="Фотография",
        help_text="Загрузите фотографию участника Услуга."
    )

    descriptions = models.TextField(
        verbose_name=_("Описания"),
        help_text=_("Описания услуги")
    )
    view_count = models.PositiveIntegerField(default=0, verbose_name=_("Количество просмотров."))

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Service, self).save(*args, **kwargs)

    def increment_view_count(self):
        self.view_count += 1
        self.save(update_fields=['view_count'])

    class Meta:
        verbose_name = _("Услуга")
        verbose_name_plural = _("Услуги")
