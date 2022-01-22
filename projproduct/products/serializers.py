from products.models import ProductDetails
from rest_framework import serializers


# Serializers define the API representation.
class ProductDetailsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProductDetails
        fields = ['id', 'name', 'price', 'quantity']