from modeltranslation.translator import TranslationOptions, register

from projects.models import (
     News, About, Service, Review
)




@register(About)
class AboutTranslationOptions(TranslationOptions):
    fields = ('title', 'content')


@register(News)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'short_description', 'long_description',)





@register(Service)
class ServiceTranslationOptions(TranslationOptions):
    fields = ('title', 'descriptions')


@register(Review)
class ReviewTranslationOptions(TranslationOptions):
    fields = ('full_name', "description")
