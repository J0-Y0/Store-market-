from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include
from debug_toolbar.toolbar import debug_toolbar_urls
from django.views.generic import TemplateView
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)


urlpatterns = [
    path("", TemplateView.as_view(template_name="common/index.html")),
    path("admin/", admin.site.urls),
    path("auth/", include("djoser.urls")),
    path("auth/", include("djoser.urls.jwt")),
    path("store/", include("store.urls")),
    path("reaction/", include("common.urls")),
    # api documentation
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    # Optional UI:
    path(
        "api/schema/swagger-ui/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "api/schema/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
]

if settings.DEBUG:
    urlpatterns += debug_toolbar_urls()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # urlpatterns += [path("silk/", include("silk.urls", namespace="silk"))]


admin.site.site_header = "e-Market | Administration"
admin.site.index_title = "Admin"
admin.site.site_title = "e-Market"
