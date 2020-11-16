from django.urls import path
from . import views

urlpatterns = [
    path('', views.time_data_now),
    path('<str:ts>', views.time_data),
    
]