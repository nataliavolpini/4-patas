from django.contrib import admin
from django.urls import path


from nuestros_4patas.views import saludar_usuario
from app_perfiles.views import  registro, login_view, CustomLogoutView, MiPerfilUpdateView


urlpatterns = [
    path('', saludar_usuario, name= "saludar usuario"),
    # URLS Usuario y sesion
    path('signup/', registro, name="registro"),
    path('login/', login_view, name="login"),
    path('logout/', CustomLogoutView.as_view(), name="logout"),
    path('profile/', MiPerfilUpdateView.as_view(), name="editar_perfil"),
]    