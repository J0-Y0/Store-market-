from django.contrib import admin
from django.urls import path, include
from debug_toolbar.toolbar import debug_toolbar_urls

urlpatterns = [
    path("admin/", admin.site.urls),
    path("auth/", include("djoser.urls")),
    path("store/", include("store.urls")),
    path("reaction/", include("common.urls")),
] + debug_toolbar_urls()

admin.site.site_header = "e-Market | Administration"
admin.site.index_title = "Admin"
admin.site.site_title = "e-Market"
