from django.test import TestCase

from app_blog.models import Perro

# Create your tests here.
class PerroTests(TestCase):
    """En esta clase van todas las pruebas del modelo Perro."""

    def test_creacion_perro(self):
        # caso uso esperado
        perro = Perro(nombre="Lobo", raza="golden", fecha_nacimiento="2023-11-15", descripcion= "jugueton")
        perro.save()

        # Compruebo que el curso fue creado y la data fue guardad correctamente
        self.assertEqual(Perro.objects.count(), 1)
        self.assertEqual(perro.nombre, "Lobo")
        self.assertEqual(perro.raza, "golden")
        self.assertEqual(perro.fecha_nacimiento, "2023-11-15")
        self.assertEqual(perro.descripcion, "jugueton")

