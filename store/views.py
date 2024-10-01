from django.shortcuts import get_object_or_404
from django.db.models import Count, F
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework import status
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.mixins import (
    RetrieveModelMixin,
    CreateModelMixin,
    DestroyModelMixin,
)
from django_filters.rest_framework import DjangoFilterBackend
from .models import *
from .serializers import *
from .filter import ProductFilter
from common.serializers import *


class ProductViewSet(ModelViewSet):
    serializer_class = ProductSerializer

    queryset = Product.objects.all()
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = ProductFilter
    search_fields = ["title"]
    ordering_fields = ["price"]

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


class ProductCommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer

    def get_queryset(self):
        product_id = self.kwargs["product_pk"]
        return Comment.objects.filter(
            content_type__model="product", object_id=product_id
        )

    def get_serializer_context(self):
        return {"object_id": self.kwargs["product_pk"], "model_name": "product"}


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


class CartVewSet(
    RetrieveModelMixin, DestroyModelMixin, CreateModelMixin, GenericViewSet
):
    serializer_class = CartSerializer
    queryset = Cart.objects.prefetch_related("items__product").all()


class CartItemViewSet(ModelViewSet):
    serializer_class = CartItemSerializer

    def get_queryset(self):
        query_set = CartItem.objects.all()
        cart_id = self.kwargs.get("cart_pk")
        if cart_id is not None:
            query_set = query_set.filter(cart_id=cart_id)

        return query_set
