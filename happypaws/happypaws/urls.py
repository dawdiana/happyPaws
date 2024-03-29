"""
URL configuration for happypaws project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from webserviceapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuarios/register/', views.formulario_registro),
    path('usuarios/login/', views.inicio_sesion),
    path('usuarios/<int:id>/editar_perfil/', views.editar_perfil),
    path('usuarios/logout/', views.logout),
    path('animales', views.pagAcogida),
    path('animales/<int:id_solicitado>', views.pagInfAnimales_solicitado), #encontramos a los animales mediante la id asignada
    path('productos', views.pagProductos),
    path('productos/<int:id_solicitado>', views.pagInfProducto_solicitado),
    path('noticias', views.pagNoticias),
]

