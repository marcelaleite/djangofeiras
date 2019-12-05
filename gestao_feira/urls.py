from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from gestao_feira.views import (feira_list_view, feira_detail_view, feira_create_view, feira_update_view, feira_delete_view,
organizadores_list_view, organizadores_detail_view, organizadores_create_view, organizadores_update_view, organizadores_delete_view,
patrocinadores_list_view, patrocinadores_detail_view, patrocinadores_create_view, patrocinadores_update_view,
patrocinadores_delete_view, observacoes_list_view, observacoes_detail_view, observacoes_create_view, observacoes_update_view,
observacoes_delete_view, instituicao_list_view, instituicao_detail_view, instituicao_create_view, instituicao_update_view,
instituicao_delete_view, categoria_list_view, categoria_detail_view, categoria_create_view, categoria_update_view,
categoria_delete_view, home_view, sobre_view)

urlpatterns = [
    path('', home_view, name='home'),
    path('sobre', sobre_view, name='sobre'),

    path('feira/', feira_list_view,name='feira-list'),
    path('feira/<int:pid>/', feira_detail_view,name='feira-detail'),
    path('feira/<int:pid>/update/', feira_update_view,name='feira-update'),
    path('feira/new', feira_create_view,name='feira-create'),
    path('feira/<int:pid>/delete/', feira_delete_view,name='feira-delete'),

    path('organizadores/', organizadores_list_view,name='organizadores-list'),
    path('organizadores/<int:pid>/', organizadores_detail_view,name='organizadores-detail'),
    path('organizadores/<int:pid>/update/', organizadores_update_view,name='organizadores-update'),
    path('organizadores/new/', organizadores_create_view,name='organizadores-create'),
    path('organizadores/<int:pid>/delete/', organizadores_delete_view,name='organizadores-delete'),

    path('patrocinadores/', patrocinadores_list_view,name='patrocinadores-list'),
    path('patrocinadores/<int:pid>/', patrocinadores_detail_view,name='patrocinadores-detail'),
    path('patrocinadores/<int:pid>/update/', patrocinadores_update_view,name='patrocinadores-update'),
    path('patrocinadores/new/', patrocinadores_create_view,name='patrocinadores-create'),
    path('patrocinadores/<int:pid>/delete/', patrocinadores_delete_view,name='patrocinadores-delete'),

    path('observacoes/', observacoes_list_view,name='observacoes-list'),
    path('observacoes/<int:pid>/', observacoes_detail_view,name='observacoes-detail'),
    path('observacoes/<int:pid>/update/', observacoes_update_view,name='observacoes-update'),
    path('observacoes/new/', observacoes_create_view,name='observacoes-create'),
    path('observacoes/<int:pid>/delete/', observacoes_delete_view,name='observacoes-delete'),

    path('instituicao/', instituicao_list_view,name='instituicao-list'),
    path('instituicao/<int:pid>/', instituicao_detail_view,name='instituicao-detail'),
    path('instituicao/<int:pid>/update/', instituicao_update_view,name='instituicao-update'),
    path('instituicao/new/', instituicao_create_view,name='instituicao-create'),
    path('instituicao/<int:pid>/delete/', instituicao_delete_view,name='instituicao-delete'),

    path('categoria/', categoria_list_view,name='categoria-list'),
    path('categoria/<int:pid>/', categoria_detail_view,name='categoria-detail'),
    path('categoria/<int:pid>/update/', categoria_update_view,name='categoria-update'),
    path('categoria/new/', categoria_create_view,name='categoria-create'),
    path('categoria/<int:pid>/delete/', categoria_delete_view,name='categoria-delete'),
]
