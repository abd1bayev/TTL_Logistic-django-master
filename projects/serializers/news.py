from rest_framework import serializers

from projects.models import News


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['id', 'title', 'short_description', 'long_description', 'image', 'slug', 'view_count', 'created_time',
                  'updated_time']
        read_only_fields = ['id', 'created_time', 'updated_time']
