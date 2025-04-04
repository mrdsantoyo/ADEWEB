from django.urls import path
from . import views

urlpatterns = [
    path('', views.crear_documento, name='crear_documento'),
    path('exito/', views.documento_exito, name='documento_exito'),
]
