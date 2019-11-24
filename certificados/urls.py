"""certificado URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from django.conf import settings

from certificados.views import *

urlpatterns = [
    # Nível usuário
    path('', certificados_list_view, name='certificados-list'),
    path('<int:pid>/<int:cid>/', certificados_detail_view, name='certificados-detail'),
    path('<int:pid>/<int:cid>/download/', certificados_download_view, name='certificados-download'),

    # Nível administrador (Modelos)
    path('modelos/', certificados_admin_list_view, name='certificados-model-list'),
    path('modelo/new/', certificados_admin_create_view, name='certificados-model-create'),
    path('modelo/<int:pid>/', certificados_admin_detail_view, name='certificados-model-detail'),
    path('modelo/<int:pid>/update/', certificados_admin_update_view, name='certificados-model-update'),
    path('modelo/<int:pid>/delete/', certificados_admin_delete_view, name='certificados-model-delete'),
]
