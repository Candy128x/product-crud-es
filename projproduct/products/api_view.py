from products.models import ProductDetails
from products.serializers import ProductDetailsSerializer
from rest_framework import routers, serializers, viewsets


# ViewSets define the view behavior.
class ProductDetailsApiViewSet(viewsets.ModelViewSet):
    queryset = ProductDetails.objects.all()
    serializer_class = ProductDetailsSerializer