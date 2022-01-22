from django.urls import path, include
from products.api_view import ProductDetailsApiViewSet
from rest_framework import routers

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'api', ProductDetailsApiViewSet)

urlpatterns = [
    path('', include(router.urls)),
]