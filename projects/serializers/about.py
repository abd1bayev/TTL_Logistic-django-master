from rest_framework import serializers

from projects.models import About, About_Image

from rest_framework import serializers

class AboutImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = About_Image
        fields = ['image']

class AboutSerializer(serializers.ModelSerializer):
    images = AboutImageSerializer(many=True, read_only=True)

    class Meta:
        model = About
        fields = ['id', 'content', 'images']