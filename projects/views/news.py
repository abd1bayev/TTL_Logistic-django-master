from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.response import Response

from projects.models import News
from projects.serializers.news import NewsSerializer
from projects.utils import NewsPagination


class NewsListAPIView(generics.ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    pagination_class = NewsPagination

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


class NewsRetrieveView(generics.RetrieveAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

    def get_object(self):
        slug = self.kwargs['slug']  # Get the slug from the URL
        news = get_object_or_404(News, slug=slug)
        news.increment_view_count()
        return news
