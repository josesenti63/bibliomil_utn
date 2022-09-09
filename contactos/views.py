from django.shortcuts import render
from django.views.generic import View
from django.views.generic import FormView
from contactos.models import Consulta
from contactos.forms import ConsultaForm
# Create your views here.

class Contacto(FormView):
    template_name = 'contactos/contacto.html'
    form_class = ConsultaForm
    success_url = 'mensaje_enviado'

    def form_valid(self, form):
        form.save()
        form.send_email()
        return super().form_valid(form)

class MensajeEnviado(View):
    template = 'contactos/mensaje_enviado.html'

    def get(self, request):
        params={}
        params['mensaje']= "Aqui va un mensaje"
        return render(request, self.template, params)
