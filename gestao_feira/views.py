from django.shortcuts import render, get_object_or_404,redirect

from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Feira,Organizadores,Patrocinadores,Observacoes,Instituicao
from django.contrib.auth import authenticate, login

#	FEIRA	#
def feira_list_view(request):
	obj = Feira.objects.all()
	contexto = {
		'object': obj
	}
	return render(request,'feira/list_view.html',contexto)

def feira_detail_view(request, pid):
	obj = get_object_or_404(Feira, id=pid)
	contexto = {
		'object': obj
	}
	return render(request,'feira/detail_view.html',contexto)

def feira_create_view(request):
    form = FeiraForm(request.POST or None)

    if form.is_valid():
        form.save()
        form = FeiraForm()

    contexto = {
        'form' : form
    }
    return render(request, 'feira/create_view.html', contexto)

def feira_update_view(request, pid):
    obj = get_object_or_404(Feira, id=pid)
    form = FeiraForm(request.POST or None, instance = obj)

    if form.is_valid():
        form.save()

    contexto = {
        'form' : form
    }
    return render(request, 'feira/create_view.html', contexto)

def feira_delete_view(request, pid):
    obj = get_object_or_404(Feira, id=pid)

    if request.method == 'POST':
        obj.delete()
        return redirect('../../')

    contexto = {
        'object' : obj
    }
    return render(request, 'feira/delete_view.html', contexto)

#	ORGANIZADORES	#
def organizadores_list_view(request):
	obj = Organizadores.objects.all()
	contexto = {
		'object': obj
	}
	return render(request,'organizadores/list_view.html',contexto)

def organizadores_detail_view(request, pid):
	obj = get_object_or_404(Organizadores, id=pid)
	contexto = {
		'object': obj
	}
	return render(request,'organizadores/detail_view.html',contexto)

def organizadores_create_view(request):
    form = OrganizadoresForm(request.POST or None)

    if form.is_valid():
        form.save()
        form = OrganizadoresForm()

    contexto = {
        'form' : form
    }
    return render(request, 'organizadores/create_view.html', contexto)

def organizadores_update_view(request, pid):
    obj = get_object_or_404(Organizadores, id=pid)
    form = OrganizadoresForm(request.POST or None, instance = obj)

    if form.is_valid():
        form.save()

    contexto = {
        'form' : form
    }
    return render(request, 'organizadores/create_view.html', contexto)

def organizadores_delete_view(request, pid):
    obj = get_object_or_404(Organizadores, id=pid)

    if request.method == 'POST':
        obj.delete()
        return redirect('../../')

    contexto = {
        'object' : obj
    }
    return render(request, 'organizadores/delete_view.html', contexto)

#	PATROCINADORES	#
def patrocinadores_list_view(request):
	obj = Patrocinadores.objects.all()
	contexto = {
		'object': obj
	}
	return render(request,'patrocinadores/list_view.html',contexto)

def patrocinadores_create_view(request):
    form = PatrocinadoresForm(request.POST or None)

    if form.is_valid():
        form.save()
        form = PatrocinadoresForm()

    contexto = {
        'form' : form
    }
    return render(request, 'patrocinadores/create_view.html', contexto)

def patrocinadores_detail_view(request, pid):
	obj = get_object_or_404(Patrocinadores, id=pid)
	contexto = {
		'object': obj
	}
	return render(request,'patrocinadores/detail_view.html',contexto)

def patrocinadores_update_view(request, pid):
    obj = get_object_or_404(Patrocinadores, id=pid)
    form = PatrocinadoresForm(request.POST or None, instance = obj)

    if form.is_valid():
        form.save()

    contexto = {
        'form' : form
    }
    return render(request, 'patrocinadores/create_view.html', contexto)

def patrocinadores_delete_view(request, pid):
    obj = get_object_or_404(Patrocinadores, id=pid)

    if request.method == 'POST':
        obj.delete()
        return redirect('../../')

    contexto = {
        'object' : obj
    }
    return render(request, 'patrocinadores/delete_view.html', contexto)

#	OBSERVACOES	#
def observacoes_list_view(request):
	obj = Observacoes.objects.all()
	contexto = {
		'object': obj
	}
	return render(request,'observacoes/list_view.html',contexto)

def observacoes_detail_view(request, pid):
	obj = get_object_or_404(Observacoes, id=pid)
	contexto = {
		'object': obj
	}
	return render(request,'observacoes/detail_view.html',contexto)

def observacoes_create_view(request):
    form = ObservacoesForm(request.POST or None)

    if form.is_valid():
        form.save()
        form = ObservacoesForm()

    contexto = {
        'form' : form
    }
    return render(request, 'observacoes/create_view.html', contexto)

def observacoes_update_view(request, pid):
    obj = get_object_or_404(Observacoes, id=pid)
    form = ObservacoesForm(request.POST or None, instance = obj)

    if form.is_valid():
        form.save()

    contexto = {
        'form' : form
    }
    return render(request, 'observacoes/create_view.html', contexto)

def observacoes_delete_view(request, pid):
    obj = get_object_or_404(Observacoes, id=pid)

    if request.method == 'POST':
        obj.delete()
        return redirect('../../')

    contexto = {
        'object' : obj
    }
    return render(request, 'observacoes/delete_view.html', contexto)

#	INSTITUIÇÃO	#
def instituicao_list_view(request):
	obj = Instituicao.objects.all()
	contexto = {
		'object': obj
	}
	return render(request,'instituicao/list_view.html',contexto)

def instituicao_detail_view(request, pid):
	obj = get_object_or_404(Instituicao, id=pid)
	contexto = {
		'object': obj
	}
	return render(request,'instituicao/detail_view.html',contexto)

def instituicao_create_view(request):
    form = InstituicaoForm(request.POST or None)

    if form.is_valid():
        form.save()
        form = InstituicaoForm()

    contexto = {
        'form' : form
    }
    return render(request, 'instituicao/create_view.html', contexto)

def instituicao_update_view(request, pid):
    obj = get_object_or_404(Instituicao, id=pid)
    form = InstituicaoForm(request.POST or None, instance = obj)

    if form.is_valid():
        form.save()

    contexto = {
        'form' : form
    }
    return render(request, 'instituicao/create_view.html', contexto)

def instituicao_delete_view(request, pid):
    obj = get_object_or_404(Instituicao, id=pid)

    if request.method == 'POST':
        obj.delete()
        return redirect('../../')

    contexto = {
        'object' : obj
    }
    return render(request, 'instituicao/delete_view.html', contexto)
