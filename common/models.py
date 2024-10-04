from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.db import models
from django.conf import settings


# Base model to handle generic content relationships
class GenericContent(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()  # ID of the content object
    content_object = GenericForeignKey(
        "content_type", "object_id"
    )  # Generic foreign key to any content
    created_at = models.DateTimeField(
        auto_now_add=True
    )  # Timestamp when the record is created

    class Meta:
        abstract = True  # This will not create a separate table in the database


# Comment Model
class Comment(GenericContent):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )  # User who made the comment
    comment_text = models.CharField(max_length=500)  # The comment content


# Like Model
class Like(GenericContent):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )  # The user who liked the content

    class Meta:
        unique_together = (
            "user",
            "content_type",
            "object_id",
        )  # Ensure a user can only like a piece of content once


# Tag Model
class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)  # Tag name (must be unique)

    def __str__(self) -> str:
        return self.name


# Content-Tag Relationship Model
class ContentTag(GenericContent):
    tag = models.ForeignKey(
        Tag, on_delete=models.CASCADE
    )  # Tag associated with the content
