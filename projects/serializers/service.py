from rest_framework import serializers

from projects.models.service import Service,ServiceImage


class ServiceImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceImage
        fields = ['id','image']

class ServiceSerializer(serializers.ModelSerializer):
    images = ServiceImageSerializer(many=True, source='images_service')

    class Meta:
        model = Service
        fields = ['id', 'title', 'slug', 'descriptions', 'images']
