import re
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth import login

# Create your views here.
#Se crea la primera vista que sera enlace al registro
def pagina_login(request):
    params = {}
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        user=authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("catalogo")
        else:
            return render(request, "usuarios/login.html")
    return render(request, "usuarios/login.html", params)
    

