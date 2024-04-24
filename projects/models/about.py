from django.db import models
from django.utils.translation import gettext_lazy as _


class About(models.Model):

    content = models.TextField(
        verbose_name="Содержание",
        help_text="Введите содержание для объекта."
    )



    def __str__(self):
        return self.content

    class Meta:
        verbose_name = _("О нас")
        verbose_name_plural = _("О нас (множественное число)")




class About_Image(models.Model):
    about = models.ForeignKey(About, on_delete=models.CASCADE, related_name='images_about')
    image = models.ImageField(
                            verbose_name=_("Imageabout"),
                            upload_to='about_images/',
                        )