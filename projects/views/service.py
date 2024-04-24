from django.shortcuts import get_object_or_404
from rest_framework.generics import RetrieveAPIView, ListAPIView
from rest_framework.response import Response

from projects.models.service import Service
from projects.serializers.service import ServiceSerializer
from projects.utils import ServicePagination



class ServiceListAPIView(ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

class ServiceRetrieveView(RetrieveAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

    def get_object(self):
        slug = self.kwargs['slug']
        return get_object_or_404(Service, slug=slug)