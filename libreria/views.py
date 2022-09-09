from django.shortcuts import render
from django.shortcuts import redirect
from catalogo.models import Libro
from libreria.forms import CargarForm
from django.http import Http404
from django.views.generic import View
from django.views.generic import TemplateView
# Create your views here.
def cargar_imagen(request):
    params ={}
    
    if request.method == "POST":
        form=CargarForm(request.POST, request.FILES)
        params['form']=form
        if form.is_valid():
            titulo_libro=form.cleaned_data['titulo_libro']
            autor_libro=form.cleaned_data['autor_libro']
            tapa_libro=form.cleaned_data['tapa_libro']

            nuevo_libro = Libro(titulo_libro=titulo_libro, autor_libro=autor_libro, tapa_libro=tapa_libro)
            nuevo_libro.save()
            return redirect('index')


    else:
        form = CargarForm()
        params['form']= form
        return render(request, 'libreria/formulario.html', params)

class VerImagenes(View): 
    template = "libreria/verimagenes.html"

    def get(self, request):
        params={}
        try:
            libros = Libro.objects.all()
        except Libro.DoesNotExist:
            raise Http404
        params["libros"]= libros

        return render(request, self.template, params)
def ver_imagen(request, libro_id):
    params={}
    try:
        libro = Libro.objects.get(pk=libro_id)
    except Libro.DoesNotExist:
        raise Http404
    params["libro"] = libro
    
    return render(request, "libreria/verimagen.html", params)

class AboutView(TemplateView):
    template_name = "about.html"
