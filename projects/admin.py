from django.contrib import admin
from django.db import models
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _
from modeltranslation.admin import TranslationAdmin
from tinymce.widgets import TinyMCE

from .models import About, ContactInformation, Partner, Review
from .models import TeamMember
from .models.contact import ContactFormView
from .models.news import News
from .models.publications import Publication
from .models.service import Service


class AboutAdmin(TranslationAdmin):
    # Specify which fields to display in the admin list view
    list_display = ('title', 'created_at', 'updated_at')

    # Add the TinyMCE editor for the 'content' field
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
    }

    # Specify fields to use for filtering in the admin list view
    list_filter = ('created_at', 'updated_at')

    # Specify fields to use for searching in the admin list view
    search_fields = ('title', 'content')


# Register the About model with the custom AboutAdmin
admin.site.register(About, AboutAdmin)


class TeamMemberAdmin(TranslationAdmin):
    list_display = ('first_name', 'last_name', 'position', 'image_preview')
    search_fields = ('first_name', 'last_name', 'position', 'sphere_of_activity', 'education', 'scientific_degree')
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
    }
    prepopulated_fields = {'slug': ('first_name',)}

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" alt="{}" height="50"/>', obj.image.url,
                               f"{obj.first_name} {obj.last_name}")
        return 'No Image'

    image_preview.allow_tags = True
    image_preview.short_description = 'Изображение'


admin.site.register(TeamMember, TeamMemberAdmin)


class PublicationAdmin(TranslationAdmin):
    list_display = ('title', 'team_member')
    list_filter = ('team_member',)
    prepopulated_fields = {"slug": ("title",)}  # new

    # Add TinyMCE editor for the 'content' field
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
    }


admin.site.register(Publication, PublicationAdmin)


class NewsAdmin(TranslationAdmin):
    list_display = ('title', 'display_short_description', 'image_preview')  # Include the custom method
    search_fields = ('title', 'short_description', 'long_description')
    prepopulated_fields = {"slug": ("title",)}

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
    }

    def display_short_description(self, obj):
        # Use format_html to mark the short_description as safe HTML
        return format_html(obj.short_description)

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" alt="{}" height="150"/>', obj.image.url, "Image Preview")
        return 'No Image'

    image_preview.allow_tags = True
    image_preview.short_description = 'Изображение'

    display_short_description.short_description = 'Short Description'  # Custom column name


admin.site.register(News, NewsAdmin)


class ContactInformationAdmin(admin.ModelAdmin):
    list_display = ('address', 'phone_number', 'email')
    search_fields = ('address', 'phone_number', 'email', 'landmark')
    list_filter = ('transportation',)

    fieldsets = (
        ('Контактные данные', {
            'fields': ('address', 'phone_number', 'email')
        }),
        ('Информация о местоположении', {
            'fields': ('landmark', 'transportation')
        }),
    )

    def has_add_permission(self, request):
        # Check if any address already exists in the database
        return not ContactInformation.objects.exists()

    def has_delete_permission(self, request, obj=None):
        # Disable the delete action to prevent deleting instances
        return False

    def has_change_permission(self, request, obj=None):
        # Allow change permission only for the existing address data
        if obj is not None:
            return ContactInformation.objects.filter(address=obj.address).exists()
        return super().has_change_permission(request, obj)


admin.site.register(ContactInformation, ContactInformationAdmin)


class ServiceAdmin(TranslationAdmin):
    # Specify which fields to display in the admin list view
    list_display = ('title', 'display_short_description', 'image_preview', 'created_time', 'updated_time')
    prepopulated_fields = {"slug": ("title",)}

    # Add TinyMCE editor for the 'descriptions' field
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
    }

    # Define a method to display a truncated version of descriptions in the admin list view
    def display_short_description(self, obj):
        # Use format_html to mark the short_description as safe HTML
        return format_html(obj.descriptions)

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" alt="{}" height="150"/>', obj.image.url, "Image Preview")
        return 'No Image'

    image_preview.allow_tags = True
    image_preview.short_description = 'Изображение'

    display_short_description.short_description = 'Описание'

    # Add filtering options
    list_filter = ('created_time', 'updated_time')

    # Add search fields
    search_fields = ('title', 'descriptions')


# Register the Service model with the custom admin class
admin.site.register(Service, ServiceAdmin)


class ContactFormViewAdmin(admin.ModelAdmin):
    # Specify which fields to display in the admin list view
    list_display = ('first_name', 'last_name', 'email', 'message')

    # Add the TinyMCE editor for the 'message' field
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
    }

    # Optionally, you can specify fields to search on in the admin interface
    search_fields = ('first_name', 'last_name', 'email')


admin.site.register(ContactFormView, ContactFormViewAdmin)


class PartnerAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'url')
    search_fields = ('title', 'url')
    list_filter = ('title',)
    list_per_page = 20

    fieldsets = (
        (_('Основная информация'), {
            'fields': ('title', 'image', 'url'),
        }),
    )

    class Meta:
        verbose_name = _("Партнер")
        verbose_name_plural = _("Партнеры")


admin.site.register(Partner, PartnerAdmin)


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'service', 'is_active')


admin.site.register(Review, ReviewAdmin)
