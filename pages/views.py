from django.shortcuts import get_object_or_404, render, redirect
from django.template import context

from .forms import Utilisateurforms
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from new_project.models import Etudiant, Professeur
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
#deconnexion
def deconnexion(request):
    logout(request)
    return redirect('connexion')


def dashboardadmin(request):
    etudiants = Etudiant.objects.all()
    nombre_total_admin = Etudiant.objects.count()
    recherche = request.GET.get('recherche')
    if recherche:
        etudiants = etudiants.filter(nom__icontains=recherche)
    context = {
        'etudiants':etudiants,
        'nombre_total_admin':nombre_total_admin
    }
   
    
    return render(request,'pages/dashboardadmin.html', context)

# def dashboardteacher(request):
#     etudiants = Etudiant.objects.all()
#     nombre_total_admin = Etudiant.objects.count()

#     context = {
#         "etudiants": etudiants,
#         "nombre_total_admin": nombre_total_admin,
#     }

#     return render(request, "dashboardteacher/dashboardteacher.html", context)
def dashboardteacher(request):
    professeur = get_object_or_404(Professeur, id_user=request.user)
    context = {"professeur": professeur}
    return render(request, "dashboardteacher/dashboardteacher.html", context)



def dashboardstudent(request):

    return render(request, 'dashboardstudent/dashboardstudent.html')

# vue generic en django










   