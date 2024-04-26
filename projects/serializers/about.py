from rest_framework import serializers

from projects.models import About, About_Image

from rest_framework import serializers

class AboutImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = About_Image
        fields = ['id','image']

class AboutSerializer(serializers.ModelSerializer):
    images = AboutImageSerializer(many=True, source='images_about')

    class Meta:
        model = About
        fields = ['id', 'content', 'images']
        
        