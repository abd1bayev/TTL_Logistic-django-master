from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination


class CustomPagination(PageNumberPagination):
    page_size = 0
    page_size_query_param = "page_size"
    max_page_size = 100
    # cursor_query_param = "cursor"
    # ordering_fields = ["created_time", "name"]


class TeamPagination(CustomPagination):
    pass


class PublicationPagination(CustomPagination):
    pass


class NewsPagination(CustomPagination):
    pass


class ServicePagination(CustomPagination):
    pass


class SearchResultsPagination(LimitOffsetPagination):
    default_limit = 10
    max_limit = 100
