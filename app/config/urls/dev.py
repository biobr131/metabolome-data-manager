from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from debug_toolbar.toolbar import debug_toolbar_urls
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView, SpectacularRedocView

urlpatterns = [
    path("dev/", include("accounts.urls.dev")),
    path("dev/admin/", admin.site.urls),
    path("dev/silk/", include("silk.urls", namespace="silk")),
    path("dev/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("dev/docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
    path("dev/redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
] + debug_toolbar_urls()

if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATICFILES_DIRS
    )
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
