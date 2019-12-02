from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, FileResponse, HttpResponseForbidden
from django.core.exceptions import PermissionDenied

import io
from reportlab.pdfgen import canvas

from .gerador.dadosCertificado import DadosCertificado
from .gerador.dadosCertificadoAssinatura import DadosCertificadoAssinatura
from .gerador.geradorCertificado import GeradorCertificado
from .gerador.certificadoHelpers import *

from .models import Certificado
from .forms import CertificadoForm

from gestao_feira.models import Feira
from gestao_presenca.models import Atividade, Cronograma, Inscricao, Pessoa

# Create your views here.

#
# Lista todos os certificados que o usuário teve participação.
#
@login_required
def certificados_list_view(request):
    # Verifica se o usuário está logado corretamente, senão emite notificação de permição negada.
    if (not request.user.is_authenticated):
        raise PermissionDenied()

    #Classe auxiliar para armazenar as informações de certificados disponíveis
    class CertificadoLista:
        def __init__(self, id, id_feira, nome_feira, id_categoria, nome_categoria):
            self.id = id
            self.id_feira = id_feira
            self.nome_feira = nome_feira
            self.id_categoria = id_categoria
            self.nome_categoria = nome_categoria

    certificados = []  # Lista dos certificados encontrados
    feiras_id = []     # Lista das feiras com participação (para evitar duplicação de certificados)

    #Busca todas as inscrições em que o usuário teve participação
    inscricoes = Inscricao.objects.filter(usuario__id=request.user.id, participou=True)

    #Percorre as inscrições encontradas (se existirem), para criar a lista de certificados disponíveis para o usuário
    i = 1
    for inscricao in inscricoes:
        try:
            #Busca o cronograma associado a inscrição atual
            cronograma = Cronograma.objects.get(id=inscricao.cronograma.id)

            #Busca a feira associada ao cronograma atual
            feira = Feira.objects.get(id=cronograma.feira.id)

            #Verifica se a 'id' da feira atual não está na lista de feiras participadas:
            if (not feira.id in feiras_id):
                certificados.append(CertificadoLista(i, feira.id, feira.nome_feira, inscricao.categoria.id, inscricao.categoria.nome))
                feiras_id.append(feira.id)
                i = i + 1
            else: #Senão, a 'id' da feira atual já está na lista de feiras participadas:
                add = True
                #Percorre a lista de feiras participadas, testando se existe um certificado para a mesma feira e categoria registrados:
                for certificado in certificados:
                    if (certificado.id_feira == feira.id):
                        if (certificado.id_categoria == inscricao.categoria.id):
                            add = False
                #Se não foi encontrado uma ocorrência de feira e categoria na lista de feiras participadas:
                if (add == True):
                    #Adiciona o certificado a lista de certificados disponíveis
                    certificados.append(CertificadoLista(i, feira.id, feira.nome_feira, inscricao.categoria.id, inscricao.categoria.nome))
                    i = i + 1
        except Exception as e:
            print(e)
            pass

    contexto = {
        'object':certificados
    }

    return render(request, 'user_list_view.html', contexto)

#
# Pré-visualização do certificado que o usuário solicitou e que teve participação.
#
@login_required
def certificados_detail_view(request, pid, cid):
    # Verifica se o usuário está logado corretamente, senão emite notificação de permição negada.
    if (not request.user.is_authenticated):
        raise PermissionDenied()

    #Busca a feira, o modelo de certificado e as inscrições com participação, conforme a id de feira e id de cetegorias recebidas
    feira = get_object_or_404(Feira, id = pid)
    certificado = get_object_or_404(Certificado, feira=pid, categoria=cid)
    inscricoes = Inscricao.objects.filter(usuario__id=request.user.id, participou=True, categoria=cid)

    # Se usuário não possuir inscrição na feira em questão, mostra uma mensagem informando:
    if (inscricoes == None or len(inscricoes) == 0):
        contexto = {
            'nome_evento':feira.nome_feira
        }
        return render(request, 'user_detail_view.html', contexto)

    atividades = []  # Lista das atividades com participação encontradas para a feira

    #Percorre as inscrições encontradas, para criar a lista de atividades do evento participado
    for inscricao in inscricoes:
        try:
            #Busca o cronograma associado a inscrição atual
            cronograma = Cronograma.objects.get(id=inscricao.cronograma.id, feira=pid)

            #Busca a atividade associada ao cronograma atual:
            atividade = Atividade.objects.get(id=cronograma.atividade.id)

            atividades.append(atividade)
        except Exception as e:
            print(e)
            pass

    patrocinadores = Patrocinadores.objects.filter(feira=pid)

    pessoa = None
    try:
        pessoa = Pessoa.objects.get(usuario=request.user.id)
    except Exception as e:
        print(e)
        pass

    # Geração do certificado com os dados carregados
    buffer = makeCertificadoBytesIO(request.user, pessoa, certificado, feira, atividades, list(patrocinadores))

    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to show the file.
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=False, filename='certificado.pdf')

#
# Download do certificado que o usuário solicitou e que teve participação.
#
@login_required
def certificados_download_view(request, pid, cid):
    # Verifica se o usuário está logado corretamente, senão emite notificação de permição negada.
    if (not request.user.is_authenticated):
        raise PermissionDenied()

    #Busca a feira, o modelo de certificado e as inscrições com participação, conforme a id de feira e id de cetegorias recebidas
    feira = get_object_or_404(Feira, id = pid)
    certificado = get_object_or_404(Certificado, feira=pid, categoria=cid)
    inscricoes = Inscricao.objects.filter(usuario__id=request.user.id, participou=True, categoria=cid)

    # Se usuário não possuir inscrição na feira em questão, mostra uma mensagem informando:
    if (inscricoes == None or len(inscricoes) == 0):
        contexto = {
            'nome_evento':feira.nome_feira
        }
        return render(request, 'user_detail_view.html', contexto)

    atividades = []  # Lista das atividades com participação encontradas para a feira

    #Percorre as inscrições encontradas, para criar a lista de atividades do evento participado
    for inscricao in inscricoes:
        try:
            #Busca o cronograma associado a inscrição atual
            cronograma = Cronograma.objects.get(id=inscricao.cronograma.id, feira=pid)

            #Busca a atividade associada ao cronograma atual:
            atividade = Atividade.objects.get(id=cronograma.atividade.id)

            atividades.append(atividade)
        except Exception as e:
            print(e)
            pass

    patrocinadores = Patrocinadores.objects.filter(feira=pid)

    pessoa = None
    try:
        pessoa = Pessoa.objects.get(usuario=request.user.id)
    except Exception as e:
        print(e)
        pass

    # Geração do certificado com os dados carregados
    buffer = makeCertificadoBytesIO(request.user, pessoa, certificado, feira, atividades, list(patrocinadores))

    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='certificado.pdf')

#
# Lista todos os modelos de certificados cadastrados.
# --> PERMITIDO APENAS PARA FUNCIONÁRIOS <--
#
@login_required
def certificados_admin_list_view(request):
    # Verifica se o usuário está logado corretamente e possui nível de privilégio correto,
    # senão emite notificação de permição negada:
    if (not request.user.is_staff):
        raise PermissionDenied()

    obj = Certificado.objects.all()
    contexto = {
        'object':obj
    }

    return render(request, 'admin_list_view.html', contexto)

#
# Criação de novo modelo de certificado.
# --> PERMITIDO APENAS PARA FUNCIONÁRIOS <--
#
@login_required
def certificados_admin_create_view(request):
    # Verifica se o usuário está logado corretamente e possui nível de privilégio correto,
    # senão emite notificação de permição negada:
    if (not request.user.is_staff):
        raise PermissionDenied()

    form = CertificadoForm(request.POST, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            fn = form.save(commit = False)
            #fn.submetido_por = request.user
            fn.save()

        form = CertificadoForm()

    contexto = {
        'form':form
    }

    return render(request, 'admin_create_view.html', contexto)

#
# Visualização do modelo de certificado renderizado para o arquivo PDF.
# --> PERMITIDO APENAS PARA FUNCIONÁRIOS <--
#
@login_required
def certificados_admin_detail_view(request, pid):
    # Verifica se o usuário está logado corretamente e possui nível de privilégio correto,
    # senão emite notificação de permição negada:
    if (not request.user.is_staff):
        raise PermissionDenied()

    obj = get_object_or_404(Certificado, id = pid)

    if (type(obj) is not Certificado):
        contexto = {
            'object':obj
        }
        return render(request, 'admin_detail_view.html', contexto)

    # Geração do modelo de certificado para visualização
    buffer = makeCertificadoBytesIO(objModelCertificado=obj)

    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=False, filename='certificado.pdf')

#
# Atualização de dados de um modelo de certificado já cadastrado.
# --> PERMITIDO APENAS PARA FUNCIONÁRIOS <--
#
@login_required
def certificados_admin_update_view(request, pid):
    # Verifica se o usuário está logado corretamente e possui nível de privilégio correto,
    # senão emite notificação de permição negada:
    if (not request.user.is_staff):
        raise PermissionDenied()

    obj = get_object_or_404(Certificado, id = pid)
    form = CertificadoForm(request.POST or None, instance = obj)

    if form.is_valid():
        form.save()

    contexto = {
        'form':form
    }

    return render(request, 'admin_update_view.html', contexto)

#
# Exclusão do modelo de certificado.
# --> PERMITIDO APENAS PARA FUNCIONÁRIOS <--
#
@login_required
def certificados_admin_delete_view(request, pid):
    # Verifica se o usuário está logado corretamente e possui nível de privilégio correto,
    # senão emite notificação de permição negada:
    if (not request.user.is_staff):
        raise PermissionDenied()

    obj = get_object_or_404(Certificado, id = pid)

    if request.method == 'POST':
        obj.delete()
        return redirect('../../')

    contexto = {
        'object':obj
    }

    return render(request, 'admin_delete_view.html', contexto)
