from rest_framework import pagination
from rest_framework.response import Response

class CustomPagination(pagination.PageNumberPagination):
    def paginate_queryset(self, queryset, request, view=None):
        response = super().paginate_queryset(queryset, request, view)
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'count': self.page.paginator.count,
            'data': response.data
        })