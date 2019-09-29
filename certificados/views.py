from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, FileResponse
from django.shortcuts import redirect

import io
from reportlab.pdfgen import canvas

from .gerador.dadosCertificado import DadosCertificado
from .gerador.dadosCertificadoAssinatura import DadosCertificadoAssinatura
from .gerador.geradorCertificado import GeradorCertificado

from .models import Certificado
from .forms import CertificadoForm, CertificadoFormManual

# Create your views here.

def certificados_list_view(request):
    obj = Certificado.objects.all()
    contexto = {
        'object':obj
    }

    return render(request, 'user_list_view.html', contexto)

def certificados_detail_view(request, pid):
    obj = get_object_or_404(Certificado, id = pid)

    # Dados do certificado
    dadosCert = DadosCertificado(ptext=obj.ptext, imagem_fundo=obj.imagem_fundo.path, imagem_evento=obj.imagem_evento.path)

    # Geração do certificado
    certificado = GeradorCertificado(dadosCert)
    buffer = certificado.getCertificado()

    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to show the file.
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=False, filename='certificado.pdf')

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

def certificados_admin_list_view(request):
    obj = Certificado.objects.all()
    contexto = {
        'object':obj
    }

    return render(request, 'admin_list_view.html', contexto)

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

def certificados_admin_detail_view(request, pid):
    obj = get_object_or_404(Certificado, id = pid)

    if (type(obj) is not Certificado):
        contexto = {
            'object':obj
        }

        return render(request, 'admin_detail_view.html', contexto)

    # Dados do certificado
    dadosCert = DadosCertificado(ptext=obj.ptext, imagem_fundo=obj.imagem_fundo.path, imagem_evento=obj.imagem_evento.path)

    # Geração do certificado
    certificado = GeradorCertificado(dadosCert)
    buffer = certificado.getCertificado()

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

def certificados_admin_update_view(request, pid):
    obj = get_object_or_404(Certificado, id = pid)
    form = CertificadoForm(request.POST or None, instance = obj)

    if form.is_valid():
        form.save()

    contexto = {
        'form':form
    }

    return render(request, 'admin_update_view.html', contexto)

def certificados_admin_delete_view(request, pid):
    obj = get_object_or_404(Certificado, id = pid)

    if request.method == 'POST':
        obj.delete()
        return redirect('../../')

    contexto = {
        'object':obj
    }

    return render(request, 'admin_delete_view.html', contexto)
