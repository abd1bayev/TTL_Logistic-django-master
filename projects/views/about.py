from rest_framework import generics
from rest_framework.response import Response

from projects.models import About
from projects.serializers.about import AboutSerializer,AboutImageSerializer


class AboutListView(generics.ListAPIView):
    queryset = About.objects.all()
    serializer_class = AboutSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
 # Use the Response class here