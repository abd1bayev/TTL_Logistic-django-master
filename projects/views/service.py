from django.shortcuts import get_object_or_404
from rest_framework.generics import RetrieveAPIView, ListAPIView
from rest_framework.response import Response

from projects.models.service import Service
from projects.serializers.service import ServiceSerializer
from projects.utils import ServicePagination


class ServiceListAPIView(ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    pagination_class = ServicePagination

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(
            queryset,
        )
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class ServiceRetrieveView(RetrieveAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer

    def get_object(self):
        slug = self.kwargs['slug']  # Get the slug from the URL
        service = get_object_or_404(Service, slug=slug)
        service.increment_view_count()  # Increment view count here
        return service
