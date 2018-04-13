from django.conf.urls import url
from . import views

app_name = "accounts"
urlpatterns = [
    url('^novo-usuario/$', views.add_user, name='add-user'),
    url('^login-usuario/$', views.user_login, name='user-login'),
    url('^logout-usuario/$', views.user_logout, name='user-logout'),
    url('^alterar-senha/$', views.change_password, name='change-password'),
]