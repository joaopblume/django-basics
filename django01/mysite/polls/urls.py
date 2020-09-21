from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
''' Path usa os argumentos: rota,
 o template e o nome do app;'''