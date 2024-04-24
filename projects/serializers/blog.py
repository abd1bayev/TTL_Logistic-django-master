from rest_framework import serializers
from projects.models import Blog,Blog_Image


class BlogImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog_Image
        fields = ['image']

class BlogSerializer(serializers.ModelSerializer):
    images = BlogImageSerializer(many=True, read_only=True)

    class Meta:
        model = Blog
        fields = ['id', 'title', 'description', 'country', 'address', 'contact_information', 'slug', 'view_count', 'created_time', 'updated_time', 'images']
        # read_only_fields = ['id', 'created_time', 'updated_time', 'images']
