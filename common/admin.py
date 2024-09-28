from django.contrib import admin

from .models import *


common_field = ["content_object", "content_type", "created_at"]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ["comment_text"] + common_field


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ["user"] + common_field


@admin.register(ContentTag)
class ContentTagAdmin(admin.ModelAdmin):
    list_display = ["tag"] + common_field
