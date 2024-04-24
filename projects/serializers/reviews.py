from rest_framework import serializers
from projects.models.reviews import Review,Review_Image

class ReviewImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review_Image
        fields = ['image']

class ReviewSerializer(serializers.ModelSerializer):
    images = ReviewImageSerializer(many=True, read_only=True)

    class Meta:
        model = Review
        fields = ['id', 'service', 'phone_number', 'title', 'index_code', 'name', 'surname', 'address', 'note', 'description', 'mail', 'images']
        read_only_fields = ['id',]
