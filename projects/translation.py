from modeltranslation.translator import TranslationOptions, register

from projects.models import (
     Blog, About, Service, Review
)




@register(About)
class AboutTranslationOptions(TranslationOptions):
    fields = ('content',)


@register(Blog)
class BlogTranslationOptions(TranslationOptions):
    fields = ('title', 'description',) #  'country', 'address',





@register(Service)
class ServiceTranslationOptions(TranslationOptions):
    fields = ('title', 'descriptions',)


@register(Review)
class ReviewTranslationOptions(TranslationOptions):
    fields = ('name', "description",)
