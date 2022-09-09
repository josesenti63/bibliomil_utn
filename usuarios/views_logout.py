from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def pagina_logout(request):
    params = {}
    return render(request, "usuarios/logout.html", params)
