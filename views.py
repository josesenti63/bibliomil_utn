from django.shortcuts import render
from django.db.models import Q
from catalogo.models import Libro
from django.views.generic import View
# Create your views here.
#Se crea la primera vista que sera un mensaje de bienvenida

def index(request):
    params = {}
    params["nombre_sitio"] = "Libreria Militar"
    libro = Libro.objects.filter(
        Q(estado="Publicado"),
    )
    params["libro"] = libro
    print(libro)
    return render(request,'catalogo/index.html', params)
    
class TemplateTags1(View):
    template = "catalogo/templatetags1.html"
    def get(self, request):
        params = {}

        return render(request, self.template, params)

class EjemploLocalStorage(View):
    template = "catalogo/localstorage.html"

    def get(self, request):
        params={}
        try:
            libros = Libro.objects.all()
        except Libro.DoesNotExist:
            raise Http404
        params["libros"] = libros
        # ############################################# #
        # PARA INICIAR LA VARIABLE DE SESION CARRO      #
        # ############################################# #
        try:
            request.session["carro"]
        except:
            request.session["carro"] = {}
        
        return render(request, self.template, params)