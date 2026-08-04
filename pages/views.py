from django.shortcuts import render, redirect
from django.template import context
from django.views.generic import ListView
# import pages
from .forms import Utilisateurforms
from django.contrib.auth import authenticate, login
from django.contrib import messages
from new_project.models import Etudiant
from new_project.forms import EtudiantForm

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
            # print("Username :", username)
            # print("Password :", password)
            user = authenticate(request, username= username, password = password)
            print(user)
            if user is not None : 
                login(request, user)


                role = user.role
                print(role)
                if role == "admin" : 
                    
                    return redirect('dashboardadmin')
                
                
                elif role == "enseignant" :
      
                 return  redirect('dashboardteacher')

                elif role  == "etudiant":

                    return redirect('dashboardstudent')
            else:

                messages.error(request, "Nom utilisateur ou mot de passe incorrect")
             
    return render(request,'pages/connexion.html',{'form':form})


def dashboardadmin(request):
    etudiants = Etudiant.objects.all()
    context = {
        'etudiants':etudiants
    }
    
    return render(request,'pages/dashboardadmin.html', context)

def dashboardteacher(request):

    return render(request, 'dashboardteacher/dashboardteacher.html')

def dashboardstudent(request):

    return render(request, 'dashboardstudent/dashboardstudent.html')

# vue generic en django










   