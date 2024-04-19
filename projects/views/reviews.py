from rest_framework import generics, permissions
from projects.models import Review
from projects.serializers import ReviewSerializer


class ReviewListAPIView(generics.ListAPIView):
    serializer_class = ReviewSerializer
    permission_classes = (permissions.AllowAny,)

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        return Review.objects.filter(is_active=True)
