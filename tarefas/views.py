from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from django.http import HttpResponse
from .models import *

# Create your views here.
######## CATEGORIA ###########

def nova_categoria(request):
    if request.method == 'POST':
        form = CategoriaForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tarefas:categoria')
        else:
            print(form.errors)
    else:
        form = CategoriaForms()

    return render(request, 'tarefas/nova_categoria.html', {'form': form})

def lista_categoria(request):
    categorias = Categoria.objects.all()
    return render(request, 'tarefas/lista_categoria.html', {'categorias': categorias})

def delete_categoria(request, id):
    categoria = Categoria.objects.get(pk=id).delete()
    return redirect('tarefas:categoria')

def update_categoria(request, id):
    categoria = Categoria.objects.get(pk=id)
    if request.method == 'POST':
        form = Categoria(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect('tarefas:categoria')
    else:
        form = TarefaForms(instance=categoria)
        return render(request, 'tarefas/nova_categoria.html', {'form': form})

############ TAREFA ##############

def lista_tarefa(request):
    tarefas = Tarefa.objects.all()
    return render(request, 'tarefas/lista_tarefa.html', {'tarefas': tarefas})

def nova_tarefa(request):
    if request.method == 'POST':
        form = TarefaForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tarefas:lista-tarefa')
        else:
            print(form.errors)
    else:
        form = TarefaForms()
    return render(request, 'tarefas/nova_tarefa.html', {'form': form})

def delete_tarefa(request, id):
    tarefa = Tarefa.objects.get(pk = id).delete()
    return redirect('tarefas:lista-tarefa')

def update_tarefa(request, id):
    tarefa = Tarefa.objects.get(pk=id)
    if request.method == 'POST':
        form = TarefaForms(request.POST, instance=tarefa)
        if form.is_valid():
            form.save()
            return redirect('tarefas:lista-tarefa')
    else:
        form = TarefaForms(instance=tarefa)
        return render(request, 'tarefas/nova_tarefa.html', {'form': form})