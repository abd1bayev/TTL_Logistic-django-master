from django.db import models
from django.utils.translation import gettext_lazy as _

from projects.utils import BaseModel


class ContactInformation(BaseModel):
    country = models.CharField(
        max_length=255,
        verbose_name=_("Country"),
        help_text=_("Country of the contact address"),
    )
    city = models.CharField(
        max_length=255,
        verbose_name=_("City"),
        help_text=_("City of the contact address"),
    )
    address = models.CharField(
        max_length=500,
        verbose_name=_("Address"),
        help_text=_("Contact address including postal code"),
    )
    phone_number = models.CharField(
        max_length=255,
        verbose_name=_("Phone Number"),
        help_text=_("Phone number including country and city code"),
    )
    email = models.EmailField(
        verbose_name=_("Email"),
        help_text=_("Email address for communication"),
    )
    landmark = models.CharField(
        max_length=200,
        verbose_name=_("Landmark"),
        help_text=_("Nearest landmark to help locate the address"),
    )

    latitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        verbose_name=_("Latitude"),
        help_text=_("Latitude coordinate of the location"),
    )
    longitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        verbose_name=_("Longitude"),
        help_text=_("Longitude coordinate of the location"),
    )

    def __str__(self):
        return f"{self.address}, {self.city}, {self.country}"

    class Meta:
        verbose_name_plural = _("Contact Information")