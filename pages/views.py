from django.shortcuts import get_object_or_404, render, redirect
from pages.models import Utilisateur
from .forms import ModifierMotDePasseForm, Utilisateurforms
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from new_project.forms import EtudiantForm, AbsenceForm
from django.contrib.auth.decorators import login_required
from .forms import UtilisateurInfoForm,UtilisateurRoleForm
from .forms import Utilisateurforms
from new_project.models import Etudiant, Professeur, Absence





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


@login_required
def dashboardstudent(request):

    print(" etudiant connecté :", request.user)
    print("ID UTILISATEUR :", request.user.id)

    etudiant = Etudiant.objects.filter(
        id_user=request.user
    ).first()

    print("ETUDIANT TROUVÉ :", etudiant)

    return render(
        request,
        'dashboardstudent/dashboardstudent.html',
        {
            'etudiant': etudiant
        }
    )
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

@login_required

def modifier_mot_de_passe(request):

    if request.method == "POST":

        form = ModifierMotDePasseForm(user=request.user, data=request.POST)

        if form.is_valid():

            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, "Votre mot de passe a été modifié avec succès.")
            return redirect("parametres")

        else:

            messages.error(request, "Veuillez corriger les erreurs ci-dessous.")

    else:

        form = ModifierMotDePasseForm(user=request.user)

    return render(request, "modifier_mot_de_passe.html", {"form": form})

@login_required
def parametresteacher(request):

    professeur = get_object_or_404(Professeur, id_user=request.user)

    if request.method == "POST":

        form = UtilisateurInfoForm(request.POST, instance=professeur.id_user)

        if form.is_valid():

            form.save()
            messages.success(request, "Vos informations ont été modifiées avec succès.")
            return redirect("parametresteacher")

        else:

            messages.error(request, "Veuillez corriger les erreurs ci-dessous.")

    else:

        form = UtilisateurInfoForm(instance=professeur.id_user)

    context = {
        "form": form,
        "professeur": professeur
    }

    return render(request, "parametresteacher.html", context)

@login_required
def absences(request):

    professeur = get_object_or_404(Professeur, id_user=request.user)

    if request.method == "POST":
        form = AbsenceForm(request.POST)
        if form.is_valid():
            absence = form.save(commit=False)
            absence.professeur = professeur
            absence.matiere = professeur.matiere
            absence.save()
            messages.success(request, "Absence enregistrée avec succès.")
            return redirect("absences")
    else:
        form = AbsenceForm()

    liste_absences = Absence.objects.filter(professeur=professeur).order_by('-date')

    context = {
        "professeur": professeur,
        "form": form,
        "absences": liste_absences,
    }

    return render(request, "absences.html", context)


@login_required

def gestion_utilisateurs(request):
    users = Utilisateur.objects.all()
    context = {
        "users":users
    }
    return render(request, 'gestion_utilisateurs.html', context)
@login_required
def modifier_role(request, id):

    user = get_object_or_404(Utilisateur, id=id)

    if request.method == "POST":
        form = UtilisateurRoleForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, "Le rôle a été modifié avec succès.")
            return redirect('gestion_utilisateurs')
    else:
        form = UtilisateurRoleForm(instance=user)

    context = {
        "form": form,
        "user": user
    }
    return render(request, "formulaireutilisateurs.html", context)


@login_required

def supprimer_utilisateur(request, id):

    utilisateur = get_object_or_404(Utilisateur, id = id)
    utilisateur.delete()

    messages.success(request, 'utilisateur supprimer avec succès')
    return redirect("gestion_utilisateurs")
    


