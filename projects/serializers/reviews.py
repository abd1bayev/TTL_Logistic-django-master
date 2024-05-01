# serializers.py
from rest_framework import serializers
from projects.models import Review, Review_Image

class ReviewImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review_Image
        fields = ['id', 'image']
        
        
class ReviewSerializer(serializers.ModelSerializer):
    # images = ReviewImageSerializer(many=True, source='images_review')

    class Meta:
        model = Review
        fields = ['id', 'service', 'phone_number', 'title', 'index_code', 'name', 'surname', 'address', 'note', 'description', 'mail']
