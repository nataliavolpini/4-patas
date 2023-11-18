from django.contrib import admin
from django.urls import path

from app_blog.views import PerroListView
from app_blog.views import PerroCreateView
from app_blog.views import PerroDetailView
from app_blog.views import PerroUpdateView
from app_blog.views import PerroDeleteView



urlpatterns = [
    
    #url con listas basadas en clases perritos
    path("perritos/", PerroListView.as_view(), name="mostrar_perritos"),
    path("perritos/<int:pk>/", PerroDetailView.as_view(), name="ver_perritos"),
    path("crear-perritos/", PerroCreateView.as_view(), name="crear_perritos"),
    path("editar-perritos/<int:pk>/", PerroUpdateView.as_view(), name="editar_perritos"),
    path("eliminar-perritos/<int:pk>/", PerroDeleteView.as_view(), name="eliminar_perritos"),

]
