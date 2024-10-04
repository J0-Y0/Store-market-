from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseAdmin
from .models import User


@admin.register(User)
class UserAdmin(BaseAdmin):
    add_fieldsets = [
        ("Personal info", {"fields": ["first_name", "last_name", "email"]}),
        ("Authentication", {"fields": ["username", "password1", "password2"]}),
        (
            "User type",
            {
                "fields": [
                    "is_active",
                    "is_staff",
                    "is_superuser",
                ]
            },
        ),
        # ("Permissions", {"fields": ["groups", "user_permissions"]}),
    ]
    # list_prefetch_related = ["Permissions"]
