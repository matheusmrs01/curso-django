from django.conf.urls import url

from . import views
app_name = "tarefas"
urlpatterns = [
    url('^categoria/$', views.lista_categoria, name = 'categoria'),
    url('^nova-categoria/$', views.nova_categoria, name = 'nova-categoria'),
    url('^delete-categoria/(?P<id>[0-9]+)/$', views.delete_categoria, name = 'delete-categoria'),
    url('^nova-tarefa/$', views.nova_tarefa, name = 'nova-tarefa'),
    url('^lista-tarefa/$', views.lista_tarefa, name = 'lista-tarefa'),
    url('^delete-tarefa/(?P<id>[0-9]+)/$', views.delete_tarefa, name = 'delete-tarefa'),
]