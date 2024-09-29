from itertools import count
from django.shortcuts import get_object_or_404
from django.db.models import Count
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics

from rest_framework import status

from .models import Product, Collection
from .serializers import CollectionSerializer, ProductSerializer


class ProductList(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    def delete(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        try:
            product.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_405_METHOD_NOT_ALLOWED,
            )


class CollectionList(generics.ListCreateAPIView):
    serializer_class = CollectionSerializer
    queryset = Collection.objects.annotate(product_count=Count("product"))


class CollectionDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CollectionSerializer
    queryset = queryset = Collection.objects.annotate(product_count=Count("product"))

    def delete(self, request, pk):
        collection = get_object_or_404(Collection, pk=pk)
        try:
            collection.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_405_METHOD_NOT_ALLOWED,
            )
