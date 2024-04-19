from rest_framework import serializers

from projects.models import About


class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = ('id', 'title', 'content', 'created_at', 'updated_at')
        read_only_fields = ('id', 'created_at', 'updated_at')
