from re import L
from django.contrib import admin

from catalogo.models import Autor
from catalogo.models import Libro
# Register your models here.

class LibroInline(admin.TabularInline):
    model = Libro
    extra = 0

class AutorAdmin(admin.ModelAdmin):
    inlines = [LibroInline]


class LibroAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Relacion',  {'fields':['autor_libro']}),
        (
            'Datos Generales',
           {
            'fields': [
                'titulo_libro', 'estado', 'tapa_libro'
            ]
           },
        ),
    ]
    list_display = ['titulo_libro', 'estado_libro', 'tapa_libro',]
    ordering = ['titulo_libro']
    list_filter = ('titulo_libro', 'estado')
    search_fields = ('titulo_libro', 'estado')
    list_display_links = ('titulo_libro', 'estado_libro')
    @admin.display(description='Name')
    def upper_case_name(self, obj):
        return("%s %s" %(obj.titulo_libro, obj.estado)).upper()
admin.site.register(Autor, AutorAdmin)
admin.site.register(Libro, LibroAdmin)
