from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include
from debug_toolbar.toolbar import debug_toolbar_urls

urlpatterns = [
    path("admin/", admin.site.urls),
    path("auth/", include("djoser.urls")),
    path("auth/", include("djoser.urls.jwt")),
    path("store/", include("store.urls")),
    path("reaction/", include("common.urls")),
]

if settings.DEBUG:
    urlpatterns += debug_toolbar_urls() + static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )


admin.site.site_header = "e-Market | Administration"
admin.site.index_title = "Admin"
admin.site.site_title = "e-Market"
