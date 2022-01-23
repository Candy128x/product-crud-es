from django_elasticsearch_dsl_drf.serializers import DocumentSerializer
from products.es_documents import ProductDetailsDocument
from products.models import ProductDetails
from rest_framework import serializers


# # -> Serializers define the API representation.
# class ProductDetailsSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = ProductDetails
#         fields = ['id', 'name', 'price', 'quantity']


class ProductDetailsSerializer(DocumentSerializer):
    class Meta:
        document = ProductDetailsDocument
        fields = ('id', 'name', 'price', 'quantity')