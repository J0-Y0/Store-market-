from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product, OrderItem
from .serializers import ProductSerializer


@api_view(["GET", "POST"])
def productList(request):
    if request.method == "GET":
        products = Product.objects.select_related("collection").all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    elif request.method == "POST":
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response("saved")


@api_view()
def productDetail(request, id):
    product = get_object_or_404(Product, pk=id)
    serializer = ProductSerializer(product)

    return Response(serializer.data)
