from django.shortcuts import render, redirect
from django.urls import reverse
from django.db.models import Q
#Importo para las clases
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

# Create your views here.
from .models import Perro
from app_blog.forms import PerroFormulario
from django.contrib.auth.mixins import LoginRequiredMixin


def mostrar_perritos(request):
    # Traemos todos los datos guardados en la base de datos
    perritos = Perro.objects.all()
    # Enviamos esos datos al archivo html por el contexto
    return render(request, 'listar_perritos.html', {"perritos": perritos})

def crear_perritos(request):
    if request.method == "POST":
        formulario = PerroFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data  # es un diccionario
            nombre = data["nombre"]
            raza = data["raza"]
            fecha_nacimiento = data["fecha_nacimiento"]
            descripcion = data["descripcion"]
            perro = Perro(nombre=nombre, raza=raza, fecha_nacimiento=fecha_nacimiento, descripcion=descripcion)  # lo crean solo en RAM
            perro.save()  # Lo guardan en la Base de datos

        # Redirecciono al usuario a la lista de perritos
            url_exitosa = reverse('crear_perritos')  
            return redirect(url_exitosa)
    else:  # GET
        formulario = PerroFormulario()
    http_response = render(
        request=request,
        template_name='formulario_perro.html',
        context={'formulario': formulario}
    )
    return http_response

def buscar_perrito(request):
    if request.method == "POST":
        data = request.POST
        busqueda = data["busqueda"]
        # Filtro simple
        #perritos = Perro.objects.filter(nombre__icontains=busqueda)
        # Ejemplo filtro avanzado
        perritos = Perro.objects.filter(
            Q(nombre__icontains=busqueda) | Q(raza__contains=busqueda)
        )

        contexto = {
            "perritos": perritos,
        }
        http_response = render(
            request=request,
            template_name='listar_perritos.html',
            context=contexto,
        )
        return http_response
    


# Vistas de Perritos(basadas en clases)
class PerroListView(ListView):
    model = Perro
    template_name = 'listar_perritos.html'

class PerroCreateView(LoginRequiredMixin, CreateView):
    model = Perro
    template_name = "perrito_form.html"
    fields = ('nombre', 'raza', 'fecha_nacimiento', 'descripcion')
    success_url = reverse_lazy('mostrar_perritos')

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        self.object = form.save()
        # Agregamos la información del creador
        self.object.creador = self.request.user
        self.object.save()
        return super().form_valid(form)


class PerroDetailView(DetailView):
    model = Perro
    template_name = "perrito_detail.html"
    success_url = reverse_lazy('mostrar_perritos')


class PerroUpdateView(LoginRequiredMixin, UpdateView):
    model = Perro
    template_name = "perrito_form.html"
    fields = ('nombre', 'raza', 'fecha_nacimiento', 'descripcion')
    success_url = reverse_lazy('mostrar_perritos')



class PerroDeleteView(LoginRequiredMixin, DeleteView):
    model = Perro
    template_name = "perrito_confirm_delete.html"
    success_url = reverse_lazy('mostrar_perritos')
    

