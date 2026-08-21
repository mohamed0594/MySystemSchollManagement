from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from new_project.models import Etudiant, Matieres, Notes, Professeur
from .forms import AbsenceForm, EtudiantForm, ProfesseurForm, NotesForm 

from django.contrib.auth.decorators import login_required
from .forms import AbsenceForm, Professeur





def inscrire_etudiant(request):
    if request.method == "POST":
        form = EtudiantForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Étudiant enregistré avec succès.")
            return redirect("dashboardadmin")
        else:
            messages.error(request, "Informations incomplètes ou invalides !")
    else:
        form = EtudiantForm()

    return render(request, "formulaireadmin.html", {"form": form})


def supprimer_etudiant(request, id):
    etudiant = get_object_or_404(Etudiant, id=id)
    etudiant.delete()
    messages.success(request, "Étudiant supprimé avec succès !")
    return redirect("dashboardadmin")


def modifier_etudiant(request, id):
    etudiant = get_object_or_404(Etudiant, id=id)
    if request.method == "POST":
        form = EtudiantForm(request.POST, instance=etudiant)
        if form.is_valid():
            form.save()
            messages.success(request, "Étudiant modifié avec succès !")
            return redirect("dashboardadmin")
        else:
            messages.error(request, "Veuillez corriger les erreurs ci-dessous.")
    else:
        form = EtudiantForm(instance=etudiant)

    return render(request, "formulaireadmin.html", {"form": form})


# def liste_professeur(request):
#     professeurs = Professeur.objects.all()
#     return render(request, "liste_professeur.html", {"professeurs": professeurs})


def ajouter_professeur(request):
    if request.method == "POST":
        form = ProfesseurForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Professeur ajouté avec succès.")
            return redirect("liste_professeur")
        else:
            messages.error(request, "Veuillez corriger les erreurs dans le formulaire.")
    else:
        form = ProfesseurForm()

    return render(request, "formulaireteacher.html", {"form": form})


def modifier_professeur(request, id):

    professeur = get_object_or_404(Professeur, id=id)
    if request.method == "POST":
        form = ProfesseurForm(request.POST, instance=professeur)
        if form.is_valid():
            form.save()
            messages.success(request, "Professeur modifié avec succès.")
            return redirect("liste_professeur")
        else:
            messages.error(request, "Veuillez corriger les erreurs ci-dessous.")
    else:
        form = ProfesseurForm(instance=professeur)

    return render(request, "formulaireteacher.html", {"form": form})


def supprimer_professeur(request, id):
    professeur = get_object_or_404(Professeur, id=id)
    professeur.delete()
    messages.success(request, "Professeur supprimé avec succès.")
    return redirect("liste_professeur")


def liste_professeur(request):

    recherche = request.GET.get('recherche')

    if recherche:
        professeurs = Professeur.objects.filter(
            nom__icontains=recherche
        )
    else:
        professeurs = Professeur.objects.all()

    context = {
        'professeurs': professeurs,
        'recherche': recherche
    }

    return render(
        request,
        'liste_professeur.html',
        context
    )
# gestion des notes
def gestion_notes(request):

    etudiants = Etudiant.objects.all()
    notes = Notes.objects.all()

    return render(request,'gestion_notes.html',{'etudiants': etudiants,'notes': notes})
def modifier_note(request, note_id):
    note = get_object_or_404(Notes, id=note_id)

    if request.method == 'POST':
        form = NotesForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            messages.success(request, 'Note modifiée avec succès.')
            return redirect('gestion_notes')
        else:
            messages.error(request, 'Veuillez corriger les erreurs ci-dessous.')
    else:
        form = NotesForm(instance=note)

    return render(request, 'modifier_note.html', {'form': form})

def rechercher_notes(request):
    recherche = request.GET.get('query')
    notes = Notes.objects.filter(etudiant__nom__icontains=recherche) if recherche else Notes.objects.all()
    return render(request, 'gestion_notes.html', {'notes': notes, 'recherche': recherche})

def ajouter_note(request):

    if request.method == 'POST':

        etudiant_id = request.POST.get('etudiant')
        matiere_id = request.POST.get('matiere')
        note_value = request.POST.get('note')

        etudiant = get_object_or_404(
            Etudiant,
            id=etudiant_id
        )

        matiere = get_object_or_404(
            Matieres,
            id=matiere_id
        )

        Notes.objects.create(
            etudiant=etudiant,
            matiere=matiere,
            note=note_value
        )

        messages.success(
            request,
            'Note ajoutée avec succès.'
        )

        return redirect('gestion_notes')


    etudiants = Etudiant.objects.all()
    matieres = Matieres.objects.all()

    return render(
        request,
        'ajouter_note.html',
        {
            'etudiants': etudiants,
            'matieres': matieres
        }
    )

def ajouter_matiere(request):
    if request.method == 'POST':
        nom_matiere = request.POST.get('nom_matiere')
        if nom_matiere:
            Matieres.objects.create(nom=nom_matiere)
            messages.success(request, 'Matière ajoutée avec succès.')
            return redirect('gestion_notes')
        else:
            messages.error(request, 'Veuillez entrer un nom de matière valide.')

    return render(request, 'liste_professeur.html')


#GESTION DES NOTES 
