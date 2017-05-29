from django.conf.urls import url
from .api import *

urlpatterns = [
    url(r'^api/articulo/$',(ArticuloApi.as_view()), name='api_articulo'),
    url(r'^api/articulo/(?P<pk>[0-9]+)/$',(ArticuloApi.as_view()), name='api_articulo'),
    url(r'^api/clausula/$',(ClausulaApi.as_view()), name='api_clausula'),
    url(r'^api/clausula/(?P<pk>[0-9]+)/$',(ClausulaApi.as_view()), name='api_clausula'),
    url(r'^api/configuracion/$',(ConfiguracionApi.as_view()), name='api_configuracion'),
    url(r'^api/configuracion/(?P<pk>[0-9]+)/$',(ConfiguracionApi.as_view()), name='api_configuracion'),
    url(r'^api/empresa/$',(EmpresaApi.as_view()), name='api_empresa'),
    url(r'^api/empresa/(?P<pk>[0-9]+)/$',(EmpresaApi.as_view()), name='api_empresa'),
    url(r'^api/recepcion/$',(RecepcionApi.as_view()), name='api_recepcion'),
    url(r'^api/recepcion/(?P<pk>[0-9]+)/$',(RecepcionApi.as_view()), name='api_recepcion'),
    url(r'^api/servicio/$',(ServicioApi.as_view()), name='api_servicio'),
    url(r'^api/servicio/(?P<pk>[0-9]+)/$',(ServicioApi.as_view()), name='api_servicio'),
    url(r'^api/clientes/$',(ClienteApi.as_view()), name='api_clientes'),
    url(r'^api/clientes/(?P<pk>[0-9]+)/$',(ClienteApi.as_view()), name='api_clientes'),
    url(r'^api/direccionclientes/$',(DireccionClienteApi.as_view()), name='api_direccionclientes'),
    url(r'^api/direccionclientes/(?P<pk>[0-9]+)/$',(DireccionClienteApi.as_view()), name='api_direccionclientes'),
    url(r'^api/rechazaclausula/$',(RechazaClausulaApi.as_view()), name='api_rechazaclausula'),
    url(r'^api/rechazaclausula/(?P<pk>[0-9]+)/$',(RechazaClausulaApi.as_view()), name='api_rechazaclausula'),
]
