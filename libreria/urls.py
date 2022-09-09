from re import T
from django.urls import path
from django.views.generic import TemplateView
from libreria import views
from libreria.views import VerImagenes

urlpatterns = [
    path('cargar/', views.cargar_imagen, name="cargar"),
    path('<int:id>/ver/', views.ver_imagen, name="ver"),
    path('verimagenes/', VerImagenes.as_view(), name="verimagenes"),
    path('about/', TemplateView.as_view(template_name="about.html")),

]