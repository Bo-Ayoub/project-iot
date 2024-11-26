from django.urls import path
from . import views

urlpatterns = [
    path('', views.receive_temperature_humidity, name='home'),
    path('post', views.receive_temperature_humidity, name='post_temperature_humidity'),
]
