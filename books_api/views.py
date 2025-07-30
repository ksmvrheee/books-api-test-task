from rest_framework import mixins, viewsets
from .models import Book
from .serializers import BookSerializer


class BookViewSet(mixins.ListModelMixin, mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    Set of API endpoints to create, list and retrieve an info about books.

    Includes:
    - GET /books/ - get all books.
    - GET /books/{id}/ - retrieve an info about a singular book by id.
    - POST /books/ - create a book by specifying it's title, author's
        name and a year of publishing.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_queryset(self):
        queryset = Book.objects.all()
        author = self.request.query_params.get('author')

        if author:
            queryset = queryset.filter(author__iexact=author)

        return queryset
