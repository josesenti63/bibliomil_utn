from django.urls import path
from contactos import views
from contactos.views import Contacto
from contactos.views import MensajeEnviado 

urlpatterns=[
    path('', Contacto.as_view(), name="contacto"),
    path('mensaje_enviado', MensajeEnviado.as_view(), name="mensaje_enviado"),
]