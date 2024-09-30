from django.urls import path
from rest_framework import routers
from .views import CommentViewSet

router = routers.DefaultRouter()
router.register("comments", CommentViewSet, basename="comments")

urlpatterns = router.urls
