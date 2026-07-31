from django.shortcuts import render, redirect

import pages
from .forms import Utilisateurforms
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Create your views here.

def accueil(request):

    return render(request, 'pages/accueil.html')


def connexion(request):
    form = Utilisateurforms()
    if request.method == 'POST':
        form = Utilisateurforms(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username= username, password = password)
            print(user)
            if user is not None : 
                login(request, user)

                role = user.role
                print(role)
                if role == "admin": 
                    
                    return redirect('dashboardadmin')
                
                
                elif role == "enseignant" :
      
                 return  redirect('dashboardteacher')

                elif role  == "etudiant":

                    return redirect('dashboardstudent')
            else:

                messages.error(request, "Nom utilisateur ou mot de passe incorrect")
             
    return render(request,'pages/connexion.html',{'form':form})


def dashboardadmin(request):
    
    return render(request,'pages/dashboardadmin.html')

def dashboardteacher(request):

    return render(request, 'dashboardteacher/dashboardteacher.html')

def dashboardstudent(request):

    return render(request, 'dashboardstudent/dashboardstudent.html')







   