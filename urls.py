from django.urls import path
from . import views
from catalogo.views import TemplateTags1

urlpatterns = [
    path('', views.index, name='index'),
    path("templatetags1", TemplateTags1.as_view(), name="templatetags1"),
]