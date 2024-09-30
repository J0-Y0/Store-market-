from itertools import count
from django.shortcuts import get_object_or_404
from django.db.models import Count
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.viewsets import ModelViewSet

from rest_framework import status

from .models import Product, Collection
from .serializers import CollectionSerializer, ProductSerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def destroy(self, request, pk=None):
        product = get_object_or_404(Product, pk=pk)
        try:
            product.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_405_METHOD_NOT_ALLOWED,
            )


class CollectionViewSet(ModelViewSet):
    serializer_class = CollectionSerializer
    queryset = Collection.objects.annotate(product_count=Count("product"))

    def destroy(self, request, pk=None):
        collection = get_object_or_404(Collection, pk=pk)
        try:
            collection.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_405_METHOD_NOT_ALLOWED,
            )
