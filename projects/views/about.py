from rest_framework import generics

from projects.models import About
from projects.serializers.about import AboutSerializer


class AboutListView(generics.ListAPIView):
    queryset = About.objects.all()
    serializer_class = AboutSerializer
