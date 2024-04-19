from django.db import models
from django.utils.translation import gettext_lazy as _

from projects.utils import BaseModel


class ContactInformation(BaseModel):
    address = models.CharField(
        max_length=200,
        verbose_name="Адрес",
        help_text="Контактный адрес, включая почтовый индекс и город."
    )
    phone_number = models.CharField(
        max_length=20,
        verbose_name="Номер телефона",
        help_text="Номер телефона, включая код страны и города."
    )
    email = models.EmailField(
        verbose_name="Электронная почта",
        help_text="Адрес электронной почты для связи."
    )
    landmark = models.CharField(
        max_length=200,
        verbose_name="Ориентир",
        help_text="Ближайший ориентир, помогающий найти адрес."
    )
    transportation = models.CharField(
        max_length=100,
        verbose_name="Транспорт",
        help_text="Информация о ближайших вариантах транспорта."
    )

    def __str__(self):
        return self.address

    class Meta:
        verbose_name_plural = "Контактная информация"


class ContactFormView(BaseModel):
    first_name = models.CharField(
        max_length=100,
        verbose_name=_("Имя"),
        help_text=_("Введите ваше имя.")
    )

    last_name = models.CharField(
        max_length=100,
        verbose_name=_("Фамилия"),
        help_text=_("Введите вашу фамилию.")
    )

    email = models.EmailField(
        verbose_name=_("Email"),
        help_text=_("Введите ваш email.")
    )

    message = models.TextField(
        verbose_name=_("Текст сообщения"),
        help_text=_("Введите ваше сообщение.")
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = _("Форма обратной связи")
        verbose_name_plural = _("Формы обратной связи")
