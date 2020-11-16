from django.urls import path
from . import views

urlpatterns = [
      path('<str:ts>', views.time_data),
    
]