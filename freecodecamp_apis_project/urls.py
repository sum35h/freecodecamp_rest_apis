from django.contrib import admin
from django.urls import path,include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.views.generic import RedirectView


schema_view = get_schema_view(
   openapi.Info(
      title="DRE API's",
      default_version='v1',
      description="API endpoints for Freecodecamp Challanges developed with DRF",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="sumesh.6361@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)
urlpatterns = [
    path('',RedirectView.as_view(url='api/')),
    path('api/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('admin/', admin.site.urls),
    path('api/timestamp/', include('timestamp.urls')),
    path('api/whoami/',include('request_header_parser.urls'))
]

