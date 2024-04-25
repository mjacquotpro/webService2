from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Film, Category
from .serializers import FilmSerializer, CategorySerializer

class FilmViewSet(viewsets.ModelViewSet):
    queryset = Film.objects.all()
    serializer_class = FilmSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filterset_fields = ['categories']
    search_fields = ['name', 'description']
    ordering_fields = ['name', 'release_date']

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
