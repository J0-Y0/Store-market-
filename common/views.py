from django.shortcuts import render
from django.contrib.contenttypes.models import ContentType
from rest_framework.viewsets import ModelViewSet


from .serializers import CommentSerializer
from .models import Comment


# Create your views here.
class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()


# # generic comment view set
# class CommentViewSet(ModelViewSet):
#     serializer_class = CommentSerializer

#     def get_queryset(self):
#         content_type_model = self.request.headers.get("X-Content-Type")

#         # content_type_model = self.kwargs.get("content_type")
#         object_id = self.kwargs.get("object_pk")

#         # Get the content type
#         content_type = ContentType.objects.get(model="product")

#         return Comment.objects.filter(content_type=content_type, object_id=object_id)
