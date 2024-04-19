from django.db import models

from projects.utils import BaseModel


class TeamMember(BaseModel):
    first_name = models.CharField(
        max_length=100,
        verbose_name="Имя",
        help_text="Введите имя участника команды."
    )
    last_name = models.CharField(
        max_length=100,
        verbose_name="Фамилия",
        help_text="Введите фамилию участника команды."
    )
    patronymic = models.CharField(
        max_length=100,
        verbose_name="Отчество",
        help_text="Введите отчество участника команды."
    )
    position = models.CharField(
        max_length=100,
        verbose_name="Должность",
        help_text="Введите должность участника команды."
    )
    sphere_of_activity = models.TextField(
        verbose_name="Сфера деятельности",
        help_text="Введите сферу деятельности участника команды."
    )
    education = models.TextField(
        verbose_name="Образование",
        help_text="Введите информацию об образовании участника команды."
    )
    scientific_degree = models.TextField(
        verbose_name="Ученая степень",
        help_text="Введите ученую степень участника команды."
    )
    legal_practice = models.TextField(
        verbose_name="Юридическая практика",
        help_text="Введите информацию о юридической практике участника команды."
    )
    license = models.CharField(
        max_length=100,
        verbose_name="Лицензия",
        help_text="Введите номер лицензии или информацию о лицензии участника команды."
    )
    membership = models.CharField(
        max_length=100,
        verbose_name="Членство",
        help_text="Введите информацию о членстве участника команды."
    )
    languages = models.TextField(
        verbose_name="Языки",
        help_text="Введите информацию о владении языками участником команды."
    )
    image = models.ImageField(
        upload_to='team_member_images/',
        blank=True,
        null=True,
        verbose_name="Фотография",
        help_text="Загрузите фотографию участника команды."
    )
    slug = models.SlugField(
        unique=True,
        blank=True,
        null=True,
        max_length=400,
        verbose_name="Slug",
        help_text="Уникальный URL-адрес для участника команды. Автоматически создается из имени и фамилии."
    )

    class Meta:
        verbose_name = "Участник команды"
        verbose_name_plural = "Участники команды"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
