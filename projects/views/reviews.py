# views.py
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from projects.models import Review, Review_Image
from projects.serializers import ReviewSerializer, ReviewImageSerializer

class ReviewListAPIView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        review_instance = serializer.save()

        # Process images if available
        images_data = request.data.getlist('images')
        if images_data:
            for image_data in images_data:
                image_serializer = ReviewImageSerializer(data={'review': review_instance.id, 'image': image_data})
                image_serializer.is_valid(raise_exception=True)
                image_serializer.save()

        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
