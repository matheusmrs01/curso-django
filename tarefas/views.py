from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from django.http import HttpResponse
from django.contrib import messages
from .models import *
from django.contrib.auth.decorators import login_required

# Create your views here.
######## CATEGORIA ###########

@login_required
def nova_categoria(request):
    if request.method == 'POST':
        form = CategoriaForms(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.user = request.user
            f.save()
            return redirect('tarefas:categoria')
        else:
            print(form.errors)
    else:
        form = CategoriaForms()

    return render(request, 'tarefas/nova_categoria.html', {'form': form})

@login_required
def lista_categoria(request):
    categorias = Categoria.objects.filter(user = request.user)
    return render(request, 'tarefas/lista_categoria.html', {'categorias': categorias})

@login_required
def delete_categoria(request, id):
    categoria = Categoria.objects.get(pk=id)
    if categoria.user == request.user:
        categoria.delete()
    else:
        messages.error(request, 'Você não tem permissão para excluir essa categoria.')
        return render(request, 'core')
    return redirect('tarefas:categoria')

@login_required
def update_categoria(request, id):
    categoria = get_object_or_404(Categoria, id=id, user=request.user)
    if request.method == 'POST':
        form = CategoriaForms(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect('tarefas:categoria')
    else:
        form = TarefaForms(instance=categoria)
        return render(request, 'tarefas/nova_categoria.html', {'form': form})

############ TAREFA ##############
@login_required
def lista_tarefa(request):
    tarefas = Tarefa.objects.filter(user = request.user, status ='EA')
    return render(request, 'tarefas/lista_tarefa.html', {'tarefas': tarefas})

@login_required
def nova_tarefa(request):
    if request.method == 'POST':
        form = TarefaForms(user = request.user,  data = request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.user = request.user
            f.save()
            return redirect('tarefas:lista-tarefa')
        else:
            print(form.errors)
    else:
        form = TarefaForms(user = request.user)
    return render(request, 'tarefas/nova_tarefa.html', {'form': form})

@login_required
def delete_tarefa(request, id):
    tarefa = Tarefa.objects.get(pk=id)
    if tarefa.user == request.user:
        tarefa.delete()
    else:
        messages.error(request, 'Você não tem permissão para excluir essa tarefa.')
        return redirect('tarefas:lista-tarefa')
    return redirect('tarefas:lista-tarefa')

@login_required
def update_tarefa(request, id):
    tarefa = get_object_or_404(Tarefa, id=id, user=request.user)
    if request.method == 'POST':
        form = TarefaForms(user = request.user, data=request.POST, instance=tarefa)
        if form.is_valid():
            form.save()
            return redirect('tarefas:lista-tarefa')
    else:
        form = TarefaForms(user = request.user, instance=tarefa)
        return render(request, 'tarefas/nova_tarefa.html', {'form': form})

@login_required
def search(request):
    q = request.GET.get('search')
    if q is not None:
        results = Tarefa.objects.search(q, request.user)
    return render(request, 'tarefas/pagina_resultado.html', {'results':results})

@login_required
def detalhes_tarefa(request, id):
    tarefa = get_object_or_404(Tarefa, id=id, user=request.user)
    return render(request, 'tarefas/detalhes_tarefa.html', {'tarefa':tarefa})