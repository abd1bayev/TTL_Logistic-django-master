from rest_framework import serializers
from projects.models import Blog,Blog_Image


class BlogImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog_Image
        fields = ('id', 'image',)

class BlogSerializer(serializers.ModelSerializer):
    images = BlogImageSerializer(many=True, source='images_blog')

    class Meta:
        model = Blog
        fields = ['id', 'title', 'description', 'slug', 'created_time', 'updated_time', 'images'] #  'country', 'address', 
