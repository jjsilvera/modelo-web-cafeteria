from django.urls import path
from . import views # el punto indica el directorio actual

urlpatterns = [
    path('', views.services, name="services"),
    

]