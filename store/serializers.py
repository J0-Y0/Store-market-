from rest_framework import serializers
from .models import Collection


class CollectionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Collection
        fields = "__all__"


class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=255)
    price = serializers.DecimalField(max_digits=10, decimal_places=2)
    collection = CollectionSerializer()
