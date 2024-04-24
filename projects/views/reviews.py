from rest_framework import generics, permissions,status
from projects.models import Review
from projects.serializers import ReviewSerializer,ReviewImageSerializer
from rest_framework.response import Response

class ReviewListAPIView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        # Create a mutable copy of the immutable QueryDict
        mutable_data = request.data.copy()
        
        # Extract image data from request
        image_data = mutable_data.pop('image', None)
        
        # Serialize review data
        serializer = self.get_serializer(data=mutable_data)
        if serializer.is_valid():
            # Save review data
            review_instance = serializer.save()
            
            # Save image if provided
            if image_data:
                image_serializer = ReviewImageSerializer(data={'review': review_instance.id, 'image': image_data})
                if image_serializer.is_valid():
                    image_serializer.save()
                else:
                    review_instance.delete()  # Rollback the review creation if image serialization fails
                    return Response(image_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
