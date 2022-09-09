from django.contrib import admin
from .models import Consulta
from .models import Respuesta
# Register your models here.

class RespuestaInline(admin.TabularInline):
    model = Respuesta
    extra = 0

class ConsultaAdmin(admin.ModelAdmin):
    inlines =[RespuestaInline]
    list_display=['estado_respuesta', 'nombre', 'descripcion', 'mail', 'telefono','fecha']
    list_filter =['estado_respuesta', 'fecha']

admin.site.register(Consulta, ConsultaAdmin)