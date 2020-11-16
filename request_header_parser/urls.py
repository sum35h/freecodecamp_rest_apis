from django.urls import path
from . import views

urlpatterns = [
    path('', views.who_am_i),
    
]