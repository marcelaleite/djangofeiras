from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
#from home.views import home_view
from gestao_presenca.views import (atividade_list_view, atividade_detail_view, atividade_create_view, inscricao_create_view, inscricao_update_view,
 inscricao_list_view, inscricao_detail_view, atividade_update_view,atividade_delete_view, inscricao_delete_view, confirmacao_presenca, gerarQRCODE)

app_name = 'gestao_presenca'

urlpatterns = [
    path('atividade/', atividade_list_view,name='atividade-list'),
    path('atividade/<int:pid>/', atividade_detail_view,name='atividade-detail'),
    path('atividade/<int:pid>/update/', atividade_update_view,name='atividade-update'),
    path('atividade/new', atividade_create_view,name='atividade-create'),
    path('atividade/<int:pid>/delete', atividade_delete_view,name='atividade-delete'),
    path('inscricao/', inscricao_list_view,name='inscricao-list'),
    path('inscricao/<int:pid>/', inscricao_detail_view,name='inscricao-detail'),
    path('inscricao/<int:pid>/update/', inscricao_update_view,name='inscricao-update'),
    path('inscricao/new/', inscricao_create_view,name='inscricao-create'),
    path('inscricao/<int:pid>/delete', inscricao_delete_view,name='inscricao-delete'),
    path('presenca/<int:id_atividades>', gerarQRCODE,name='atividade-qrcode'),
    path('presenca/<int:id_atividades>', confirmacao_presenca,name='confirmacao')
]
