from django.urls import path
from . import views

urlpatterns = [
    path('', views.registro_usuario, name='register'),
]
