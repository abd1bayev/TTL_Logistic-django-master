from rest_framework import serializers

from projects.models.service import Service


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['id', 'title', 'slug', 'descriptions', 'image', 'view_count', 'created_time', 'updated_time']
        read_only_fields = ['id', 'created_time', 'updated_time']
