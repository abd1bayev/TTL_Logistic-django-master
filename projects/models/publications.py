from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

# from projects.models import TeamMember
from projects.utils import BaseModel


class Publication(BaseModel):
    title = models.CharField(
        max_length=200,
        verbose_name=_("Название"),
        help_text=_("Название публикации")
    )

    content = models.TextField(
        verbose_name=_("Содержание"),
        help_text=_("Содержание публикации")
    )

    team_member = models.ForeignKey(
        'TeamMember',
        on_delete=models.CASCADE,
        verbose_name=_("Участник команды"),
        help_text=_("Участник команды, связанный с публикацией")
    )

    slug = models.SlugField(
        max_length=200,
        unique=True,
        blank=True,
        verbose_name=_("URL-часть"),
        help_text=_("URL-часть публикации. Автоматически создается из названия.")
    )

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)

        super(Publication, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _("Публикация")
        verbose_name_plural = _("Публикации")
