from django.contrib import admin
from django.db import models
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _
from modeltranslation.admin import TranslationAdmin
from tinymce.widgets import TinyMCE

from .models import About, ContactInformation, About_Image, Review, Image
from .models.blog import Blog, Blog_Image  
from .models.service import Service, ServiceImage


class AboutImageInline(admin.TabularInline):
    model = About_Image
    extra = 1


@admin.register(About)
class AboutAdmin(TranslationAdmin):
    list_display = ('content_as_html',)
    search_fields = ('content',)
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},  # Matn maydonchalari uchun TinyMCE ni qo'llash
    }
    inlines = [AboutImageInline]

    def content_as_html(self, obj):
        return format_html(obj.content)

    content_as_html.short_description = 'Content'
    
    class Meta:
        order = 1

# admin.site.register(About_Image)  # Register the AboutImage model as well




class ServiceImageInline(admin.TabularInline):
    model = ServiceImage
    extra = 1

class ServiceAdmin(TranslationAdmin):
    # Specify which fields to display in the admin list view
    inlines = [ServiceImageInline]

    list_display = ('title', 'display_short_description', 'display_images', 'created_time', 'updated_time')
    prepopulated_fields = {"slug": ("title",)}

    # Add TinyMCE editor for the 'descriptions' field
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
    }


    def display_short_description(self, obj):
        # Use format_html to mark the short_description as safe HTML
        return format_html(obj.descriptions)

    # Define a method to display images in the admin list view
    def display_images(self, obj, size=25):
        image_tags = [f'<img src="{image.image.url}" alt="Image {image.id}" width="{100}" height="{100}">' for image in obj.images_service.all()]
        return format_html(''.join(image_tags))

    display_images.short_description = 'Images'  # Custom column name
    display_short_description.short_description = 'Description'  # Custom column name

    # Add filtering options
    list_filter = ('created_time', 'updated_time')

    # Add search fields
    search_fields = ('title', 'descriptions')

    class Meta:
        order = 2

# Register the Service model with the custom admin class
admin.site.register(Service, ServiceAdmin)






class ImageInline(admin.TabularInline):
    model = Blog_Image
    extra = 1  # Number of empty forms to display

class BlogAdmin(TranslationAdmin):
    list_display = ('title','address_as_html','description_as_html', 'formatted_date_created',)  # Customize the displayed fields

    def formatted_date_created(self, obj):
        return obj.created_time.strftime('%Y-%m-%d %H:%M:%S')  # Assuming created_time is the field name
    formatted_date_created.short_description = _('Date Created')  # Custom column name

    def description_as_html(self, obj):
        return format_html(obj.description)

    description_as_html.short_description = 'Description'
    
    def address_as_html(self, obj):
        return format_html(obj.address)

    address_as_html.short_description = 'Address'
    
    search_fields = ('title', 'description', 'country', 'address',)  # Add fields to search
    prepopulated_fields = {"slug": ("title",)}  # Automatically populate the slug from the title

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},  # Use TinyMCE for text fields
    }

    # def image_preview(self, obj):
    #     # Display a preview of the first image if available
    #     if obj.images.exists():
    #         first_image = obj.images.first().image.url  # Assuming Image has 'image' field
    #         return format_html('<img src="{}" alt="Image Preview" height="100"/>', first_image)
    #     return _('No Image')

    # image_preview.short_description = _('Image Preview')  # Custom column name

    inlines = [ImageInline]  # Add ImageInline to allow adding images inline with Blog
    
    class Meta:
        order = 3

admin.site.register(Blog, BlogAdmin)

# class ContactInformationAdmin(admin.ModelAdmin):
#     list_display = ('address', 'phone_number', 'email')
#     search_fields = ('address', 'phone_number', 'email', 'landmark')

#     fieldsets = (
#         (_('Contact Data'), {
#             'fields': ('country', 'city', 'address', 'phone_number', 'email')
#         }),
#         (_('Location Information'), {
#             'fields': ('landmark', 'latitude', 'longitude')
#         }),
#     )

#     def has_add_permission(self, request):
#         # Check if any address already exists in the database
#         return not ContactInformation.objects.exists()

#     def has_delete_permission(self, request, obj=None):
#         # Disable the delete action to prevent deleting instances
#         return False

#     def has_change_permission(self, request, obj=None):
#         # Allow change permission only for the existing address data
#         if obj is not None:
#             return ContactInformation.objects.filter(address=obj.address).exists()
#         return super().has_change_permission(request, obj)

# admin.site.register(ContactInformation, ContactInformationAdmin)



class ImageInline(admin.TabularInline):
    model = Image
    extra = 1

class ReviewAdmin(TranslationAdmin):
    inlines = [ImageInline]
    list_display = ['title', 'service', 'phone_number', 'mail','display_images']
    search_fields = ['title', 'service__name', 'phone_number', 'mail']
    list_filter = ['service']
    readonly_fields = ['display_images','title',]

    
    
    def display_images(self, obj, size=25):
        image_tags = [f'<img src="{image.image.url}" alt="Image {image.id}" width="{100}" height="{100}">' for image in obj.review_images.all()]
        return format_html(''.join(image_tags))
    
    
    display_images.short_description = 'Images'  # Custom column name




    class Meta:
        order = 4
        
admin.site.register(Review, ReviewAdmin)





