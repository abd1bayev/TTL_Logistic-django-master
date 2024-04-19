from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.response import Response

from projects.models import Publication
from projects.serializers import PublicationSerializer
from projects.utils import PublicationPagination


class PublicationListAPIView(generics.ListAPIView):
    queryset = Publication.objects.all()
    serializer_class = PublicationSerializer
    pagination_class = PublicationPagination

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


class PublicationRetrieveView(generics.RetrieveAPIView):
    queryset = Publication.objects.all()
    serializer_class = PublicationSerializer

    def get_object(self):
        slug = self.kwargs['slug']  # Get the slug from the URL
        return get_object_or_404(Publication, slug=slug)
