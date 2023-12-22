from django.shortcuts import render
from rest_framework import generics, pagination
from . import models, serializers

# Views for handling Product-related operations
class ProductList(generics.ListCreateAPIView):
    """
    API view for listing and creating products.

    Supports both GET (list) and POST (create) operations for products.
    """
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer
    pagination_class = pagination.PageNumberPagination

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API view for retrieving, updating, and deleting a specific product.

    Supports GET (retrieve), PUT (update), PATCH (partial update),
    and DELETE (delete) operations for a specific product.
    """
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer
    pagination_class = pagination.PageNumberPagination