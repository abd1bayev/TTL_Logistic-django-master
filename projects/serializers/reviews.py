# serializers.py
from rest_framework import serializers
from projects.models import Review, Image


# class ReviewImageSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Image
#         fields = ['id', 'image']
#
#
# class ReviewSerializer(serializers.ModelSerializer):
#     # images = ReviewImageSerializer(many=True, source='images_review')
#
#     class Meta:
#         model = Review
#         fields = ['id', 'service', 'phone_number', 'title', 'index_code', 'name', 'surname', 'address', 'note', 'description', 'mail']

class ReviewImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['id', 'image']


class ReviewSerializer(serializers.ModelSerializer):
    images = ReviewImageSerializer(many=True, read_only=True)

    class Meta:
        model = Review
        fields = ['id', 'service', 'phone_number', 'title', 'index_code', 'name', 'surname', 'address', 'note', 'description', 'mail', 'images']

    def create(self, validated_data):
        images_data = self.context['request'].FILES
        review = Review.objects.create(**validated_data)
        for image_data in images_data.values():
            Image.objects.create(review=review, image=image_data)
        return review
