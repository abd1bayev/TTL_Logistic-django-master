from django.contrib.contenttypes.models import ContentType
from django.db.models import Q
from rest_framework import generics

from projects.models import Publication, Service, News, About
from projects.serializers import SearchSerializer
from projects.utils import SearchResultsPagination


class SearchResultsView(generics.ListAPIView):
    serializer_class = SearchSerializer
    pagination_class = SearchResultsPagination

    def get_queryset(self):
        query = self.request.query_params.get('query', '')

        content_types = [
            ContentType.objects.get_for_model(model)
            for model in [News, Publication, Service]
        ]

        combined_queryset = []
        for content_type in content_types:
            model_name = content_type.model_class().__name__
            model_queryset = content_type.model_class().objects.filter(
                Q(title_ru__icontains=query) | Q(title_en__icontains=query) | Q(title_uz__icontains=query)
            ).values('id', 'title_ru', 'title_en', 'title_uz', 'slug')
            for entry in model_queryset:
                entry['content_type'] = model_name
                combined_queryset.append(entry)

        return combined_queryset

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        response.data['query'] = request.query_params.get('query', '')
        return response
