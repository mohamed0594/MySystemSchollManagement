from django.shortcuts import get_object_or_404, render, redirect
from django.template import context

from pages.models import Utilisateur

from .forms import ModifierMotDePasseForm, Utilisateurforms
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from new_project.models import Etudiant, Professeur
from new_project.forms import EtudiantForm
from django.contrib.auth.decorators import login_required
from .forms import UtilisateurInfoForm
from .forms import Utilisateurforms, UtilisateurInfoForm



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

def dashboardteacher(request):
    professeur = get_object_or_404(Professeur, id_user=request.user)

    context = {"professeur": professeur
               }
    return render(request, "dashboardteacher/dashboardteacher.html", context)



def dashboardstudent(request):

    return render(request, 'dashboardstudent/dashboardstudent.html')

# vue du parametres

@login_required
def parametres(request):

    utilisateur = request.user

    if request.method == "POST":

        form = UtilisateurInfoForm(request.POST, instance=utilisateur)

        if form.is_valid():

            form.save()
            messages.success( request,  "Vos informations ont ete modifiees avec succes.")

            return redirect("parametres")

    else:

        form = UtilisateurInfoForm(instance=utilisateur)
        context = {
                    "form": form,
                    "utilisateur": utilisateur
                }

    return render(request, "parametres.html",context )

# @login_required
# def modifier_mot_de_passe(request):

#     if request.method == "POST":

#         ancien_mot_de_passe = request.POST.get("ancien_mot_de_passe")
#         nouveau_mot_de_passe = request.POST.get("nouveau_mot_de_passe")
#         confirmation = request.POST.get("confirmation_mot_de_passe")

#         if not request.user.check_password(ancien_mot_de_passe):
#             messages.error(
#                 request,
#                 "Votre ancien mot de passe est incorrect."
#             )

#             return redirect("modifier_mot_de_passe")

#         if nouveau_mot_de_passe != confirmation:
#             messages.error(
#                 request,
#                 "Les deux nouveaux mots de passe ne correspondent pas."
#             )

#             return redirect("modifier_mot_de_passe")

#         if len(nouveau_mot_de_passe) < 8:
#             messages.error(
#                 request,
#                 "Le nouveau mot de passe doit contenir au moins 8 caractères."
#             )

#             return redirect("modifier_mot_de_passe")

#         request.user.set_password(nouveau_mot_de_passe)

#         request.user.save()

#         update_session_auth_hash(
#             request,
#             request.user
#         )

#         messages.success(
#             request,
#             "Votre mot de passe a été modifié avec succès."
#         )

#         return redirect("parametres")

#     return render(
#         request,
#         "modifier_mot_de_passe.html"
#     )