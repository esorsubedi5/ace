from rest_framework import serializers
from dataclasses import fields
from . import models

class ProductSerializer(serializers.ModelSerializer):
    """
    Serializer for the Product model.

    Serializes Product instances to and from JSON format.
    """
    class Meta:
        model = models.Product 
        fields = ['id','category','title','detail','price','product_ratings', 'size']
        depth = 1 # Set the depth directly in the Meta class for better readability

    category = serializers.PrimaryKeyRelatedField(queryset=models.Category.objects.all())
    size = serializers.PrimaryKeyRelatedField(queryset=models.Size.objects.all())

    def to_representation(self, instance):
        """
        Custom representation method for the ProductSerializer.

        Provides a custom representation for the serializer output.
        """
        representation = super().to_representation(instance)
        # manipulating the representation data before returning it
        representation['price'] = f"${instance.price:.2f}"
        return representation


 
