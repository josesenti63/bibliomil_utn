from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#Se crea la primera vista que sera un mensaje de bienvenida

def users(request):
    return HttpResponse("Bienvenido al registro de usuarios")
# Create your views here.
