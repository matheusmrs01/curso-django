from django import forms
from .models import *

class CategoriaForms(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'

class TarefaForms(forms.ModelForm):
    class Meta:
        model = Tarefa
        fields = '__all__'