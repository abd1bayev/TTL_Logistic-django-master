from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

from projects.utils import BaseModel

class Blog(BaseModel):
    title = models.CharField(
        max_length=200,
        verbose_name=_("Title"),
        help_text=_("Title of the blog post")
    )

    description = models.TextField(
        verbose_name=_("Description"),
        help_text=_("Brief description of the blog post")
    )

    country = models.CharField(
        max_length=255,
        verbose_name=_("Country"),
        help_text=_("Country of the blog post"),
        null=True,
        blank=True
    )

    address = models.TextField(
        verbose_name=_("Address"),
        help_text=_("Address of the blog post"),
        null=True,
        blank=True
    )


    slug = models.SlugField(
        max_length=200,
        unique=True,
        blank=True,
        verbose_name=_("Slug"),
        help_text=_("Slug for the URL of the blog post. Automatically generated from the title.")
    )

    view_count = models.PositiveIntegerField(default=0, verbose_name=_("View Count"))

    def __str__(self):
        return self.title

    def increment_view_count(self):
        self.view_count += 1
        self.save(update_fields=['view_count'])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Blog, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _("Blog")
        verbose_name_plural = _("Blogs")

class Blog_Image(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='images_blog')
    image = models.ImageField(
                            verbose_name=_("Imageblog"),
                            upload_to='blog_images/',
                        )
