from django import forms




class PerroFormulario(forms.Form):
    nombre = forms.CharField(required=True, max_length=64)
    raza =  forms.CharField(max_length=64)  
    fecha_nacimiento = forms.DateField(required=True)
    descripcion = forms.CharField(max_length=50000)

