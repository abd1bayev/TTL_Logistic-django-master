from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

from projects.utils import BaseModel


class News(BaseModel):
    title = models.CharField(
        max_length=200,
        verbose_name=_("Заголовок"),
        help_text=_("Заголовок новости")
    )

    short_description = models.TextField(
        verbose_name=_("Краткое описание"),
        help_text=_("Краткое описание новости")
    )

    long_description = models.TextField(
        verbose_name=_("Полное описание"),
        help_text=_("Полное описание новости")
    )

    image = models.ImageField(
        upload_to='news_images/',
        blank=True,
        null=True,
        verbose_name="Фотография",
        help_text="Загрузите фотографию участника Новости."
    )

    slug = models.SlugField(
        max_length=200,
        unique=True,
        blank=True,
        verbose_name=_("URL-часть"),
        help_text=_("URL-часть публикации. Автоматически создается из названия.")
    )
    view_count = models.PositiveIntegerField(default=0, verbose_name=_("Количество просмотров."))

    def __str__(self):
        return self.title

    def increment_view_count(self):
        self.view_count += 1
        self.save(update_fields=['view_count'])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        super(News, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _("Новость")
        verbose_name_plural = _("Новости")
