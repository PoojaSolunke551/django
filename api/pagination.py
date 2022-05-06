from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination,CursorPagination

class MyPageNumberPagination(PageNumberPagination):
    page_size = 5