from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.generators import OpenAPISchemaGenerator
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from django.conf.urls.i18n import i18n_patterns
from config.settings import (
    base as settings,
    django_settings_module,
)


class BothHttpAndHttpsSchemaGenerator(OpenAPISchemaGenerator):
    def get_schema(self, request=None, public=False):
        schema = super().get_schema(request, public)
        schema.schemes = (
            ["http"] if django_settings_module == "development" else ["https"]
        )
        return schema


schema_view = get_schema_view(
    openapi.Info(
        "ABSOLVO BONA FIDES",
        "v1.0",
        'Project name: "ABSOLVO BONA FIDES"',
        contact=openapi.Contact(
            name="technovision.uz",
            url="https://technovision.uz",
        ),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
    # generator_class=BothHttpAndHttpsSchemaGenerator,
)

urlpatterns = [

    path('admin/', admin.site.urls),
    # path('api/v1/', include('projects.urls'))

]

if django_settings_module in ("development", "staging"):
    urlpatterns += [
        path(
            "swagger/",
            schema_view.with_ui("swagger", cache_timeout=0),
            name="schema-swagger-ui",
        ),
        path(
            "redoc/",
            schema_view.with_ui("redoc", cache_timeout=0),
            name="schema-redoc",
        ),
    ]

if django_settings_module == "development":
    urlpatterns += [
        path("__debug__/", include("debug_toolbar.urls")),
    ]
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT
    )
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )


urlpatterns += i18n_patterns(
    path('api/v1/', include('projects.urls')),  # Replace 'app_name' with your app's name
)