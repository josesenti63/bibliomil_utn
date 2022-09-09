from django.urls import path
from usuarios import views
from usuarios import views_login
from usuarios import views_logout
from usuarios import views_registro

urlpatterns = [
    path('', views.users, name='users'),
    path('login', views_login.pagina_login, name='login'),
    path('logout', views_logout.pagina_logout, name='logout'),
    path('login', views_registro.pagina_registro, name='registro'),
]