from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, FileResponse, HttpResponseForbidden
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect

import io
from reportlab.pdfgen import canvas

from .gerador.dadosCertificado import DadosCertificado
from .gerador.dadosCertificadoAssinatura import DadosCertificadoAssinatura
from .gerador.geradorCertificado import GeradorCertificado
from .gerador.certificadoHelpers import *

from .models import Certificado
from .forms import CertificadoForm, CertificadoFormManual

from gestao_feira.models import Feira

from gestao_presenca.models import Atividade, Cronograma, Inscricao, Pessoa
#from gestao_presenca.forms import AtividadeForm, InscricaoForm

# Create your views here.

@login_required
def certificados_list_view(request):
    obj = Certificado.objects.all()
    #obj = Inscricao.objects.all().filter(usuario__id=request.user.id, participou=True)
    print(request.user)
    print(request.user.id)
    print(request.user.username)
    print(request.user.is_authenticated)
    print(request.user.is_staff)
    print(request.user.is_superuser)
    #print(Certificado.objects.all())
    print(Inscricao.objects.all())
    print(Atividade.objects.all())
    print(Cronograma.objects.all())

    if (not request.user.is_authenticated):
        raise PermissionDenied()

    class CertificadoLista:
        def __init__(self, id, id_feira, nome_feira):
            self.id = id
            self.id_feira = id_feira
            self.nome_feira = nome_feira

    certificados = []  # Lista dos certificados encontrados
    feiras_id = []     # Lista das feiras com participação (para evitar duplicação de certificados)

    print()
    print('--> Teste busca simples')
    inscricoes = Inscricao.objects.filter(usuario__id=request.user.id, participou=True)
    print(inscricoes)
    if (inscricoes != None and len(inscricoes) > 0):
        #ativ = Atividade.objects.filter(id=inscricoes[0].atividades.id)
        #print(ativ)
        #if (ativ != None and len(ativ) > 0):
        #    feira = Feira.objects.filter(id=ativ[0].feira.id)
        #    print(feira)
        crono = Cronograma.objects.filter(atividade=inscricoes[0].atividades.id)
        print(crono)

    #for value in inscricoes:
    #    certificados.append(CertificadoLista(value.id, '???'))

    print()
    print('--> for inscricao in inscricoes:')
    i = 1
    for inscricao in inscricoes:
        atividade = Atividade.objects.filter(id=inscricao.atividades.id)
        cronograma = Cronograma.objects.filter(id=inscricoes[0].atividades.id)
        print(inscricao)
        print(atividade)
        print(cronograma)
        if (cronograma != None and len(cronograma) > 0):
            print(cronograma[0])
            feira = Feira.objects.filter(id=cronograma[0].feira.id)
            print(feira)
            if (feira != None and len(feira) > 0):
                print(feira[0].nome_feira)
                #if (not atividade[0].feira.id in feiras_id):
                if (not feira[0].id in feiras_id):
                    #certificados.append(CertificadoLista(i, atividade[0].feira.id, feira[0].nome_feira))
                    certificados.append(CertificadoLista(i, feira[0].id, feira[0].nome_feira))
                    feiras_id.append(cronograma[0].feira.id)
                    i = i + 1
                    print('=> Certificado adicionado!!!')

    print()
    print('--> ')
    #print(certificados[0].id)
    #print(certificados[0].nome_feira)
    print(feiras_id)
    #print('id' in feiras_id)

    contexto = {
        #'object':obj
        'object':certificados
    }

    return render(request, 'user_list_view.html', contexto)

@login_required
def certificados_detail_view(request, pid):
    #obj = get_object_or_404(Certificado, id = pid)
    feira = get_object_or_404(Feira, id = pid)
    certificado = get_object_or_404(Certificado, id = 1)
    inscricoes = Inscricao.objects.filter(usuario__id=request.user.id, participou=True)
    print(feira)
    print(certificado)
    print(inscricoes)

    if (inscricoes == None or len(inscricoes) == 0):
        contexto = {
            'nome_evento':feira.nome_feira
        }
        return render(request, 'user_detail_view.html', contexto)

    atividades = []  # Lista das atividades com participação encontradas para a feira

    print()
    print('--> for inscricao in inscricoes:')
    for inscricao in inscricoes:
        #atividade = Atividade.objects.filter(id=inscricao.atividades.id, feira=pid)
        #print(atividade)
        #if (atividade != None and len(atividade) > 0):
        #    print(atividade[0])
        #    atividades.append(atividade[0])
        #    print('=> Atividade adicionada!!!')
        cronograma = Cronograma.objects.filter(atividade=inscricao.atividades.id, feira=pid)
        print(cronograma)
        atividade = Atividade.objects.filter(id=inscricao.atividades.id)
        print(atividade)
        if (cronograma != None and len(cronograma) > 0 and atividade != None and len(atividade) > 0):
            print(cronograma[0])
            print(atividade[0])
            atividades.append(atividade[0])
            print('=> Atividade adicionada!!!')

    print()
    patrocinadores = Patrocinadores.objects.filter(feira=pid)
    print(patrocinadores)
    print()

    pessoa = None
    pes = Pessoa.objects.filter(usuario=request.user.id)
    print(pes)
    if (pes != None and len(pes) > 0):
        pessoa = pes[0]
        print(pessoa)
    print()

    # Dados do certificado
    #dadosCert = DadosCertificado(ptext=obj.ptext, imagem_fundo=obj.imagem_fundo.path, imagem_evento=obj.imagem_evento.path)
    #dadosCert = makeDadosCertificado(obj)

    # Geração do certificado
    #certificado = GeradorCertificado(dadosCert)
    ##certificado = makeCertificado(obj)
    ##buffer = certificado.getCertificado()
    #buffer = makeCertificadoBytesIO(obj)
    buffer = makeCertificadoBytesIO(request.user, pessoa, certificado, feira, atividades, list(patrocinadores))

    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to show the file.
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=False, filename='certificado.pdf')

@login_required
def certificados_download_view(request, pid):
    obj = get_object_or_404(Certificado, id = pid)

    # Dados do certificado
    dadosCert = DadosCertificado(ptext=obj.ptext, imagem_fundo=obj.imagem_fundo.path, imagem_evento=obj.imagem_evento.path)

    # Geração do certificado
    certificado = GeradorCertificado(dadosCert)
    buffer = certificado.getCertificado()

    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='certificado.pdf')

@login_required
def certificados_admin_list_view(request):
    #if (not request.user.is_authenticated or not request.user.is_staff or not request.user.is_superuser):
    if (not request.user.is_authenticated or not request.user.is_staff):
        #return HttpResponseForbidden()
        raise PermissionDenied()

    obj = Certificado.objects.all()
    contexto = {
        'object':obj
    }

    return render(request, 'admin_list_view.html', contexto)

@login_required
def certificados_admin_create_view(request):
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

@login_required
def certificados_admin_detail_view(request, pid):
    obj = get_object_or_404(Certificado, id = pid)

    if (type(obj) is not Certificado):
        contexto = {
            'object':obj
        }

        return render(request, 'admin_detail_view.html', contexto)

    # Dados do certificado
    #dadosCert = DadosCertificado(ptext=obj.ptext, imagem_fundo=obj.imagem_fundo.path, imagem_evento=obj.imagem_evento.path)

    # Geração do certificado
    #certificado = GeradorCertificado(dadosCert)
    #buffer = certificado.getCertificado()
    buffer = makeCertificadoBytesIO(objModelCertificado=obj)

    # Create a file-like buffer to receive PDF data.
    #buffer = io.BytesIO()

    # Create the PDF object, using the buffer as its "file."
    #p = canvas.Canvas(buffer)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    #p.drawString(100, 100, "Hello world.")

    # Close the PDF object cleanly, and we're done.
    #p.showPage()
    #p.save()

    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=False, filename='certificado.pdf')

@login_required
def certificados_admin_update_view(request, pid):
    obj = get_object_or_404(Certificado, id = pid)
    form = CertificadoForm(request.POST or None, instance = obj)

    if form.is_valid():
        form.save()

    contexto = {
        'form':form
    }

    return render(request, 'admin_update_view.html', contexto)

@login_required
def certificados_admin_delete_view(request, pid):
    obj = get_object_or_404(Certificado, id = pid)

    if request.method == 'POST':
        obj.delete()
        return redirect('../../')

    contexto = {
        'object':obj
    }

    return render(request, 'admin_delete_view.html', contexto)
