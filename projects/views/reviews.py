# views.py
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from projects.models import Review, Image
from projects.serializers import ReviewSerializer
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView


@method_decorator(csrf_exempt, name='dispatch')
class ReviewCreateAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = ReviewSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            review_instance = serializer.save()
            images_data = request.FILES.getlist('images')
            for image_data in images_data:
                try:
                    Image.objects.create(review=review_instance, image=image_data)
                except Exception as e:
                    print(f"Error saving image: {e}")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
