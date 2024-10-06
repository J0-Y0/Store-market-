from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseAdmin
from .models import User
from unfold.admin import ModelAdmin

from unfold.forms import AdminPasswordChangeForm, UserChangeForm, UserCreationForm


@admin.register(User)
class UserAdmin(BaseAdmin, ModelAdmin):
    compressed_fields = True
    form = UserChangeForm
    add_form = UserCreationForm
    change_password_form = AdminPasswordChangeForm
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
    # list_prefetch_related = ["Permissions"]]

    readonly_fields = ["last_login", "date_joined"]
