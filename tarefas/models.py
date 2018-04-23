from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class TarefaManager(models.Manager):
    def search(self, query, user):
        return self.get_queryset().filter(models.Q(nome__icontains=query) | models.Q(descricrao__icontains=query) | models.Q(prioridade__icontains=query) | models.Q(categoria__nome__icontains=query), user=user)

class Categoria(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Nome')
    descricrao = models.TextField(verbose_name='Descrição')
    user = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.nome

class Tarefa(models.Model):
    PRIORIDADE_CHOICES = (
        ('B', 'Baixa'),
        ('M', 'Média'),
        ('A', 'Alta'),
    )
    STATUS_CHOICES = (
        ('EA', 'Em Andamento'),
        ('C', 'Concluído'),
        ('CD', 'Cancelada'),
    )
    nome = models.CharField(max_length=100, verbose_name='Nome')
    descricrao = models.TextField(verbose_name='Descrição', blank=True)
    data_final = models.DateField(verbose_name='Data Final')
    prioridade = models.CharField(verbose_name='Prioridade', max_length=1, choices=PRIORIDADE_CHOICES)
    categoria = models.ForeignKey(Categoria, verbose_name='Categoria', on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    status = models.CharField(verbose_name='Status', max_length=2, choices=STATUS_CHOICES, blank=True, default='EA')

    objects = TarefaManager()

    def __str__(self):
        return self.nome