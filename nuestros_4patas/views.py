from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse

def saludar_usuario(request):
    contexto = {

    }
    http_response = render(
        request=request,
        template_name='inicio.html',
        context=contexto,
    )
    return http_response


def acerca_de_mi(request):
    contexto = {

    }
    http_response = render(
        request=request,
        template_name='acerca_de_mi.html',
        context=contexto,
    )
    return http_response