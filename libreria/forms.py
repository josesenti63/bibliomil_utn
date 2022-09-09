from django.forms import ModelForm
from catalogo.models import Libro

class CargarForm(ModelForm):
    class Meta:
        model=Libro
        fields = ['titulo_libro', 'autor_libro', 'tapa_libro']

    def __init__(self,*args, **kwargs):
        super(CargarForm, self).__init__(*args, **kwargs)
