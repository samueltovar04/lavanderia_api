"""lavanderia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from customs.api import *
from usuarios.api_user import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('perfiles.urls')),
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
    url(r'^api/create_user/$', UserCreate.as_view()),
    url(r'^api/users/(?P<pk>[0-9]+)/$', UserDetail.as_view()),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
