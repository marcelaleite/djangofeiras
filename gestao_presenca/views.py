from django.shortcuts import render, get_object_or_404,redirect
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Atividade,Inscricao,Cronograma
from django.contrib.auth import authenticate, login
from hashlib import sha1
from datetime import datetime
from .forms import CronogramaForm, AtividadeForm, InscricaoForm

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
			fn.save()
	form = InscricaoForm()
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

@login_required
def confirmacao_presenca(request, id_atividades, hash):

	obj = get_object_or_404(Inscricao,cronograma=id_atividades, usuario = request.user)
	cron =  get_object_or_404(Cronograma, id=obj.cronograma_id)
	mensagem = 'Você não está confirmado!'

	if cron.hash == hash:
		mensagem = 'Você está confirmado!'

	Inscricao.objects.filter(pk=obj.pk).update(participou = True, cronograma = id_atividades)
	obj.refresh_from_db()

	contexto = {
		'mensagem':mensagem,
	}
	#template_name = 'gestao_presenca/QRcode.html'
	#confirmacao_presenca = Inscricao.objects.get(pk=id)
	return render(request,'inscricao/confirmacao.html',contexto)

@login_required
def gerarQRCODE(request, id_atividades):
	obj = get_object_or_404(Cronograma,id=id_atividades)
	s = obj.data.strftime('%d/%m/%y %H:%M:%S')+datetime.now().strftime('%d/%m/%y %H:%M:%S')
	hash = sha1(s.encode('utf-8')).hexdigest()
	save_hash(hash, id_atividades)
	link = request.build_absolute_uri(reverse('gestao_presenca:confirmacao',kwargs={'id_atividades':id_atividades, 'hash':hash}))
	contexto = {
	'hash':hash,
	'link':link
	}
	return render(request,'cronograma/QRcode.html',contexto)
	#return HttpResponse(request, 'confirmacao_presenca/QRcode.html',contexto)

def erro404(request, mensagem):
	contexto = {}
	contexto = {"project_name":settings.PROJECT_NAME}
	return render(request,'gestao_presenca/erro404.html',contexto)

#	CRONOGRAMA	#
def cronograma_list_view(request):
	obj = Cronograma.objects.all()
	contexto = {
		'object': obj
	}
	return render(request,'cronograma/list_view.html',contexto)

def cronograma_detail_view(request, pid):
	obj = get_object_or_404(Cronograma, id=pid)
	contexto = {
		'object': obj
	}
	return render(request,'cronograma/detail_view.html',contexto)

def cronograma_create_view(request):
    form = CronogramaForm(request.POST or None)

    if form.is_valid():
        form.save()
        form = CronogramaForm()

    contexto = {
        'form' : form
    }
    return render(request, 'cronograma/create_view.html', contexto)

def cronograma_update_view(request, pid):
    obj = get_object_or_404(Cronograma, id=pid)
    form = CronogramaForm(request.POST or None, instance = obj)

    if form.is_valid():
        form.save()

    contexto = {
        'form' : form
    }
    return render(request, 'cronograma/update_view.html', contexto)

def cronograma_delete_view(request, pid):
    obj = get_object_or_404(Cronograma, id=pid)

    if request.method == 'POST':
        obj.delete()
        return redirect('../../')

    contexto = {
        'object' : obj
    }
    return render(request, 'cronograma/delete_view.html', contexto)

def save_hash(phash, id):
	obj = get_object_or_404(Cronograma, id=id)
	Cronograma.objects.filter(pk=obj.pk).update(hash = phash)
	#obj.update(hash = phash)
	obj.refresh_from_db()
	#self.assertEqual(obj.id)
