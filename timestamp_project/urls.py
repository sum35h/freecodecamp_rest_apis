from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/timestamp/', include('timestamp.urls')),
    path('api/whoami/',include('request_header_parser.urls'))
]

