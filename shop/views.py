from django.shortcuts import render
from rest_framework import generics, pagination
from . import models, serializers
# Create your views here.
class ProductList(generics.ListCreateAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer
    pagination_class = pagination.PageNumberPagination

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer
    pagination_class = pagination.PageNumberPagination