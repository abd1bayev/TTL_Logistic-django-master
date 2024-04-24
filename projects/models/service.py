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



    descriptions = models.TextField(
        verbose_name=_("Описания"),
        help_text=_("Описания услуги")
    )

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Service, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _("Услуга")
        verbose_name_plural = _("Услуги")
        
        
class ServiceImage(models.Model):
    image = models.ImageField(
        upload_to='service_images/',
        verbose_name=_("Image"),
        help_text=_("Image associated with the service"),
    )
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='images_service')


    def __str__(self):
        return str(self.image)
