from rest_framework.pagination import LimitOffsetPagination

class LargeResultsSetPagination(LimitOffsetPagination):
    page_size = 1000
    page_size_query_param = 'page_size'
    max_page_size = 10000

class StandardResultsSetPagination(LimitOffsetPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 1000