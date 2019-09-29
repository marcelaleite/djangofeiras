from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.shortcuts import redirect

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
    contexto = {
        'object':obj
    }

    return render(request, 'user_detail_view.html', contexto)

def certificados_download_view(request, pid):
    obj = get_object_or_404(Certificado, id = pid)
    contexto = {
        'object':obj
    }

    return render(request, 'user_detail_view.html', contexto)

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
    contexto = {
        'object':obj
    }

    return render(request, 'admin_detail_view.html', contexto)

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
