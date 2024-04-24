from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.response import Response

from projects.models import Blog
from projects.serializers.blog import BlogSerializer
from projects.utils import BlogPagination


class BlogListAPIView(generics.ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    pagination_class = BlogPagination

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


class BlogRetrieveView(generics.RetrieveAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

    def get_object(self):
        slug = self.kwargs['slug']  # Get the slug from the URL
        news = get_object_or_404(News, slug=slug)
        news.increment_view_count()
        return news
