"""
URL configuration for nuestros_4patas project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from app_blog.views import mostrar_perritos 
from nuestros_4patas.views import saludar_usuario, acerca_de_mi


urlpatterns = [
    path('admin/', admin.site.urls),
    path("pages/", include ("app_blog.urls")),
    path("", saludar_usuario, name="inicio"),
    path("accounts/", include ("app_perfiles.urls")),
    path("about/", acerca_de_mi, name="acerca-de-mi"),
    
]
