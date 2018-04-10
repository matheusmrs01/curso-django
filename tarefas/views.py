from django.shortcuts import render
from .forms import *
from django.http import HttpResponse
from django.template.loader import render_to_string

# Create your views here.

def nova_categoria(request):
    if request.method == 'POST':
        form = CategoriaForms(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Categoria adicionada com Sucesso!')
        else:
            print(form.errors)
    else:
        form = CategoriaForms()

    return render(request, 'tarefas/nova_categoria.html', {'form': form})

def nova_tarefa(request):
    if request.method == 'POST':
        form = TarefaForms(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Tarefa adicionada com sucesso!')
        else:
            print(form.errors)
    else:
        form = CategoriaForms()
    return render(request, 'tarefas/nova_tarefa.html', {'form': form})