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
        ("Authentication", {"fields": ["password1", "password2"]}),
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

    readonly_fields = ["last_login", "date_joined", "username"]
    list_display = [
        "first_name",
        "last_name",
        "email",
        "is_staff",
        "is_active",
    ]

    # def get_fieldsets(self, request, obj=None):
    #     if obj:  # Change view
    #         return self.change_fieldsets
    #     return self.add_fieldsets  # Add view


from django.contrib.auth.admin import GroupAdmin as BaseGroupAdmin
from django.contrib.auth.models import Group

admin.site.unregister(Group)


@admin.register(Group)
class GroupAdmin(BaseGroupAdmin, ModelAdmin):
    pass
