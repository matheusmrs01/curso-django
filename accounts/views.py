from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from .forms import UserForm
from django.contrib import messages
from django.http import HttpResponse
# Create your views here.

def add_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            u = form.save()
            u.set_password(u.password)
            u.save()
            messages.success(request, 'Usuário criado com sucesso! Utilize o formulario abaixo para fazer login!')
            return redirect('accounts:user-login')
        else:
            messages.error(request, form.errors)
    else:
        form = UserForm()
    return render(request, 'accounts/user_add.html', {'form':form})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            return redirect(request.GET.get('next', '/'))
        else:
            messages.error(request, 'Usuario ou senha invalidos!')
    return render(request, 'accounts/user_login.html')

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Senha alterada com sucesso!')
            return redirect('accounts:change-password')
        else:
            messages.error(request, 'Não foi possivel alterar sua senha, verifique os dados!')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'accounts/change_password.html', {'form':form})

def user_logout(request):
    logout(request)
    return redirect('accounts:user-login')
