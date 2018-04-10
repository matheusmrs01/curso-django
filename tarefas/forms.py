from django import forms
from .models import *

class CategoriaForms(forms.ModelForm):
    nome = forms.CharField(widget=forms.TextInput(attrs = {'class' : 'form-control'}))
    descricrao = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    class Meta:
        model = Categoria
        fields = '__all__'

class TarefaForms(forms.ModelForm):
    class Meta:
        model = Tarefa
        fields = '__all__'