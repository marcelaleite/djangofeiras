from django.shortcuts import render, get_object_or_404,redirect

from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Atividade,Inscricao
from django.contrib.auth import authenticate, login

def atividade_list_view(request):
	obj = Atividade.objects.all()
	contexto = {
		'object': obj
	}
	return render(request,'atividade/list_view.html',contexto)

def inscricao_list_view(request):
	obj = Inscricao.objects.all()
	contexto = {
		'object': obj
	}
	return render(request,'inscricao/list_view.html',contexto)

def atividade_detail_view(request,pid):
	#obj = Submissao.objects.get(id=pid)
	obj = get_object_or_404(Atividade,id=pid)
	contexto = {
		'object': obj
	}
	return render(request,'atividade/detail_view.html',contexto)

def inscricao_detail_view(request,pid):
	obj = get_object_or_404(Inscricao,id=pid)
	contexto = {
		'object': obj
	}
	return render(request,'inscricao/detail_view.html',contexto)

def atividade_create_view(request):
	form = AtividadeForm(request.POST or None)
	if form.is_valid():
		form.save()
		form = AtividadeForm()
	contexto = {
		'form': form
	}
	return render(request,'atividade/create_view.html',contexto)

def inscricao_create_view(request):
	if request.method == 'POST':
		form = InscricaoForm(request.POST, request.FILES or None,initial={'submetido_por': request.user})
		if form.is_valid():
			fn = form.save(commit=False)
			fn.submetido_por = request.user
			fn.save()
	form = SubmissaoForm()
	contexto = {
		'form': form
	}
	return render(request,'inscricao/create_view.html',contexto)

def atividade_update_view(request, pid):
	obj = get_object_or_404(Atividade,id=pid)
	form = AtividadeForm(request.POST or None,instance=obj)
	if form.is_valid():
		form.save()
	contexto = {
		'form': form
	}
	return render(request,'atividade/create_view.html',contexto)

def inscricao_update_view(request, pid):
	obj = get_object_or_404(Inscricao,id=pid)
	form = InscricaoForm(request.POST or None,instance=obj)
	if form.is_valid():
		form.save()
	contexto = {
		'form': form
	}
	return render(request,'inscricao/create_view.html',contexto)

def atividade_delete_view(request,pid):
	obj = get_object_or_404(Atividade,id=pid)
	if request.method == 'POST':
		obj.delete()
		return redirect('../../')
	contexto = {
		'form': form
	}
	return render(request,'atividade/delete_view.html',contexto)

def inscricao_delete_view(request,pid):
	obj = get_object_or_404(Inscricao,id=pid)
	if request.method == 'POST':
		obj.delete()
		return redirect('../../')
	contexto = {
		'form': form
	}
	return render(request,'inscricao/delete_view.html',contexto)


def confirmacao_presenca(request, id, hash):
	#template_name = 'gestao_presenca/QRcode.html'
	#confirmacao_presenca = Inscricao.objects.get(pk=id)
	username = request.USER
	user = authenticate(request, username=username)
	if user is not None:
		login(request,user)
		return render(request,'presenca/QRcode.html',contexto)

