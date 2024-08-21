from django.urls import path, include
from . import views

app_name = 'wikiApp'

urlpatterns = [
    path('',views.directorio,name='directorio'),
    path('nuevoTema',views.nuevoTema,name='nuevoTema'),
    path('nuevoArticulo',views.nuevoArticulo, name='nuevoArticulo'),
    path('vistaArticulo/<str:idTema>',views.vistaArticulo,name='vistaArticulo'),
    path('vistaDetalleArticulo/<str:idArticulo>',views.vistaDetalleArticulo,name='vistaDetalleArticulo'),
]