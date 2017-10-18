from rest_framework import pagination


class PageNumberPagination(pagination.PageNumberPagination):
    page_size = 20

    # max_page_size = 100

    def paginate_queryset(self, queryset, request, view=None):
        if request.GET.get("page", None) is None:
            return None
        return super(PageNumberPagination, self).paginate_queryset(queryset, request, view)
