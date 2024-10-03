from django.contrib import admin
from django.urls import path, include
from debug_toolbar.toolbar import debug_toolbar_urls

urlpatterns = [
    path("admin/", admin.site.urls),
    path("auth/", include("djoser.urls")),
    path("auth/", include("djoser.urls.jwt")),
    path("store/", include("store.urls")),
    path("reaction/", include("common.urls")),
] + debug_toolbar_urls()

admin.site.site_header = "e-Market | Administration"
admin.site.index_title = "Admin"
admin.site.site_title = "e-Market"


#     "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyODE2MDcxMCwiaWF0IjoxNzI3OTg3OTEwLCJqdGkiOiI4YzFhNDNkNjY4ZTk0MjkwOGVmOWNjY2NiZDdkMzNmMyIsInVzZXJfaWQiOjF9.2AKe8tTyoyejfKgfYRuVvkJIwuY6qtcHvFXCRXj6j5o",
#     "access":
#         "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzI4MDc0MzEwLCJpYXQiOjE3Mjc5ODc5MTAsImp0aSI6Ijk5NjM0MTU4M2Y0ZTQyMTViMDIxZTUwYmZlN2RjMWYwIiwidXNlcl9pZCI6MX0.rVoqoQQNMTMhtnrMhRnoigoU4FbPCBKNkyaUBtWAkm0"
# }
