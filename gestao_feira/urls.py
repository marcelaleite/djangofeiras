from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
#from home.views import home_view

urlpatterns = [
    path('feira/', feira_list_view,name='feira-list'),
    path('feira/<int:pid>/', feira_detail_view,name='feira-detail'),
    path('feira/<int:pid>/update/', feira_update_view,name='feira-update'),
    path('feira/new', feira_create_view,name='feira-create'),
    path('feira/<int:pid>/delete', feira_delete_view,name='feira-delete'),

    path('cronograma/', cronograma_list_view,name='cronograma-list'),
    path('cronograma/<int:pid>/', cronograma_detail_view,name='cronograma-detail'),
    path('cronograma/<int:pid>/update/', cronograma_update_view,name='cronograma-update'),
    path('cronograma/new/', cronograma_create_view,name='cronograma-create'),
    path('cronograma/<int:pid>/delete', cronograma_delete_view,name='cronograma-delete'),

    path('organizadores/', organizadores_list_view,name='organizadores-list'),
    path('organizadores/<int:pid>/', organizadores_detail_view,name='organizadores-detail'),
    path('organizadores/<int:pid>/update/', organizadores_update_view,name='organizadores-update'),
    path('organizadores/new/', organizadores_create_view,name='organizadores-create'),
    path('organizadores/<int:pid>/delete', organizadores_delete_view,name='organizadores-delete'),

    path('patrocinadores/', patrocinadores_list_view,name='patrocinadores-list'),
    path('patrocinadores/<int:pid>/', patrocinadores_detail_view,name='patrocinadores-detail'),
    path('patrocinadores/<int:pid>/update/', patrocinadores_update_view,name='patrocinadores-update'),
    path('patrocinadores/new/', patrocinadores_create_view,name='patrocinadores-create'),
    path('patrocinadores/<int:pid>/delete', patrocinadores_delete_view,name='patrocinadores-delete'),

    path('observacoes/', observacoes_list_view,name='observacoes-list'),
    path('observacoes/<int:pid>/', observacoes_detail_view,name='observacoes-detail'),
    path('observacoes/<int:pid>/update/', observacoes_update_view,name='observacoes-update'),
    path('observacoes/new/', observacoes_create_view,name='observacoes-create'),
    path('observacoes/<int:pid>/delete', observacoes_delete_view,name='observacoes-delete'),

    path('instituicao/', instituicao_list_view,name='instituicao-list'),
    path('instituicao/<int:pid>/', instituicao_detail_view,name='instituicao-detail'),
    path('instituicao/<int:pid>/update/', instituicao_update_view,name='instituicao-update'),
    path('instituicao/new/', instituicao_create_view,name='instituicao-create'),
    path('instituicao/<int:pid>/delete', instituicao_delete_view,name='instituicao-delete'),
]