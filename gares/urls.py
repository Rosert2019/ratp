from django.urls import path
from . import views

urlpatterns = [

    path('', views.ratp_gares, name='ratp_gare'),
 
]