from rest_framework import serializers
from dataclasses import fields
from . import models

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product 
        fields = ['id','category','title','detail','price','product_ratings', 'size']

    def __init__(self, *args, **kwargs):
        super(ProductSerializer, self).__init__(*args, **kwargs)
        self.Meta.depth = 1

    category = serializers.PrimaryKeyRelatedField(queryset=models.Category.objects.all())
    size = serializers.PrimaryKeyRelatedField(queryset=models.Size.objects.all())
 