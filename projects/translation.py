from modeltranslation.translator import TranslationOptions, register

from projects.models import (
    TeamMember, News, About, Publication, Service, Review
)


@register(TeamMember)
class TeamMemberTranslationOptions(TranslationOptions):
    fields = [
        'first_name', 'last_name', 'patronymic', 'position',
        'sphere_of_activity', 'education', 'scientific_degree',
        'legal_practice', 'license', 'membership', 'languages'
    ]


@register(About)
class AboutTranslationOptions(TranslationOptions):
    fields = ('title', 'content')


@register(News)
class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'short_description', 'long_description',)


@register(Publication)
class PublicationTranslationOptions(TranslationOptions):
    fields = ('title', 'content',)


@register(Service)
class ServiceTranslationOptions(TranslationOptions):
    fields = ('title', 'descriptions')


@register(Review)
class ReviewTranslationOptions(TranslationOptions):
    fields = ('full_name', "description")
