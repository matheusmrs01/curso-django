from django.conf.urls import url

from . import views
app_name = "tarefas"
urlpatterns = [
    url('^nova-categoria/$', views.nova_categoria, name = 'nova-categoria'),
    url('^nova-tarefa/$', views.nova_tarefa, name = 'nova-tarefa'),
]