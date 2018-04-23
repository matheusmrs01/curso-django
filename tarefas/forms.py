from django import forms
from .models import *

class CategoriaForms(forms.ModelForm):
    class Meta:
        model = Categoria
        exclude = ('user',)

class TarefaForms(forms.ModelForm):
    class Meta:
        model = Tarefa
        exclude = ('user',)

    def __init__(self, user=None, *args, **kwargs):
        super(TarefaForms, self).__init__(*args, **kwargs)
        if user is not None:
            self.fields['categoria'].queryset = Categoria.objects.filter(user = user)