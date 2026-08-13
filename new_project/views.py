from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

from new_project.models import Etudiant, Matieres, Notes, Professeur
from .forms import EtudiantForm, ProfesseurForm, NotesForm


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
    notes = Notes.objects.all()
    return render(request, 'gestion_notes.html', {'notes': notes})

def ajouter_note(request):
    if request.method == 'POST':
        etudiant_id = request.POST.get('etudiant')
        matiere_id = request.POST.get('matiere')
        note_value = request.POST.get('note')

        etudiant = get_object_or_404(Etudiant, id=etudiant_id)
        matiere = get_object_or_404(Matieres, id=matiere_id)

        note = Notes(etudiant=etudiant, matiere=matiere, note=note_value)
        note.save()

        messages.success(request, 'Note ajoutée avec succès.')
        return redirect('gestion_notes')

    etudiants = Etudiant.objects.all()
    matieres = Matieres.objects.all()
    return render(request, 'ajouter_note.html', {'etudiants': etudiants, 'matieres': matieres})


