from django.shortcuts import redirect, render
from django.contrib.auth import get_user_model, login, logout, authenticate
from django.contrib.auth.decorators import permission_required
from django.contrib import messages
from .forms import *
from baiboly.views  import home
from .fls import *
import datetime
import os
import subprocess
from django.http import HttpResponse
from django.views import View
User = get_user_model()
current_link=os.getcwd()

def User_profils(request):
    return render(request, 'user_profil.html')

def telecharge_fichier(request):   
    a=time.asctime()
    a=a.split(' ')
    b=a[3].split(':')
    b="".join(b)
    
    backup_file = f'db_out'
    backup_file_=f"{backup_file}.sqlite3"
    #
    
    if os.path.exists(f"{current_link}//{backup_file}.sqlite3"):
        backup_path = f"{current_link}//{backup_file}.sqlite3"  
        os.remove(backup_path)
        export_files_in_database(backup_file)
        backup_path = f"{current_link}//{backup_file}.sqlite3"  
    else:
        export_files_in_database(backup_file)
        backup_path = f"{current_link}//{backup_file}.sqlite3"  
    
    with open(backup_path, 'rb') as f:
        response = HttpResponse(f.read(), content_type='application/x-sqlite3')
        response['Content-Disposition'] = f'attachment; filename={backup_file_}'
    return response
   
def Appsignup(request):
    form = AuthForm()
    if request.method == 'POST':
        form = AuthForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Création de votre compte est réussi')
            return redirect('App_signin')
        else:
            return render(request, 'signup.html',{'form':form})
    else:
        form = AuthForm()
        return render (request, 'signup.html',{'form':form})
    
def Appsignin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            messages.success(request, 'Bienvenue dans votre compte')
            return redirect('index')
        else:
            messages.error(request,"Authentification échouée")  
            return render(request, 'login.html')
    else: 
        return render (request, 'login.html')

def Appsignout(request):
    logout(request)
    return redirect(home)