from django.urls import path
from rest_framework import routers
from .views import CommentViewSet, sendmail

router = routers.DefaultRouter()
router.register("comments", CommentViewSet, basename="comments")

# urlpatterns = router.urls
urlpatterns = [path("mail", sendmail)]
