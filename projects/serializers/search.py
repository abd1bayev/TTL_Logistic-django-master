from django.utils.translation import get_language
from rest_framework import serializers


class SearchSerializer(serializers.Serializer):
    content_type = serializers.CharField(max_length=20)
    id = serializers.IntegerField()

    def get_title_field(self):
        current_language = get_language()
        return f'title_{current_language}'

    def to_representation(self, instance):
        title_field = self.get_title_field()
        return {
            'content_type': instance['content_type'],
            'id': instance['id'],
            'title': instance[title_field],
            'slug': instance['slug'],
        }
