from django.db import models
from django.utils.html import format_html
# Create your models here.

class Autor(models.Model):
    nombre_autor = models.CharField(max_length=200)
    def __str__(self):
        return self.nombre_autor
class Libro(models.Model):

    En_stock = "En Stock"
    Agotado = "Agotado"
    EXISTENCIA_LIBRO =(
        (En_stock,'En Stock'),
        (Agotado,'Agotado'),
    )
    estado = models.CharField(max_length=10, choices=EXISTENCIA_LIBRO, default='En stock')
    titulo_libro = models.CharField(max_length=200)
    autor_libro = models.ForeignKey('Autor', on_delete=models.CASCADE, null=True)
    # Se define ForeignKey porque un mismo autor escribe muchos libros
    tapa_libro = models.ImageField(upload_to="catalogo/%Y/%m/%d", blank= True, null=True)
    sumario_libro = models.TextField(max_length=1000, help_text="Describa el libro")
    isbn_libro = models.CharField(max_length=13, help_text='13 Caracteres <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')

    def estado_libro(self):
        if self.estado == 'Agotado':
            return format_html('<span style="color: #FF4B36;">{}</span>', self.estado,)
        return format_html('<span style="color: #49EB6A;">{}</span>', self.estado,)

    def __str__(self, ):
       return self.titulo_libro + 'autor_libro + estado'
