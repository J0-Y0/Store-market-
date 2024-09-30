from django.contrib.contenttypes.models import ContentType

from rest_framework.serializers import ModelSerializer
from .models import *


class CommentSerializer(ModelSerializer):

    class Meta:
        model = Comment
        fields = "__all__"
        read_only_fields = ["object_id", "content_type"]

    def create(self, validated_data):
        object_id = self.context["object_id"]
        model_name = self.context["model_name"]

        content_type = ContentType.objects.get(model=model_name)
        return Comment.objects.create(
            object_id=object_id, content_type=content_type, **validated_data
        )
