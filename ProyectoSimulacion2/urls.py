"""ProyectoSimulacion2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ProyectoSimulacion2 import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Inicio),
    
    path('cuadradosMedios/',views.cuadrados_Medios),
    path('cuadradosMedios_Result/',views.cuadradosMedios),
    path('congruencialLineal/',views.congruencial_Lineal),
    path('congruencialLineal_Result/',views.congruencialLineal),
    path('transformadaInversa/',views.transformada_Inversa),
    path('transformadaInversa_Result/',views.transformadaInversa),
    path('promedioMovil/',views.promedio_Movil),
    path('promedioMovil_Result/',views.promedioMovil),
    path('alisamientoExponencial/',views.alisamiento_Exponencial),
    path('alisamientoExponencial_Result/',views.alisamientoExponencial),
    path('regresionLineal/',views.regresion_Lineal),
    path('regresionLineal_Result/',views.regresionLineal),
    path('regresionNoLineal/',views.regresion_No_Lineal),
    path('regresionNoLineal_Result/',views.regresionNoLineal),
    path('lineaDeEspera/',views.linea_De_Espera),
    path('lineaDeEspera_Result/',views.lineaDeEspera),
    path('lineaDeEsperaMontecarlo/',views.linea_De_Espera_Montecarlo),
    path('lineaDeEsperaMontecarlo_Result/',views.lineaDeEsperaMontecarlo),
]

urlpatterns+= static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
