from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404

from new_project.models import Etudiant
from .forms import EtudiantForm

def inscrire_etudiant(request):
    if request.method == "POST":
        form = EtudiantForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Étudiant enregistré avec succès.")
            return redirect("dashboardadmin")
        else:
            messages.error(request, 'Informations incomplete!')
            

    else:
        form = EtudiantForm()

    return render(request, "formulaireadmin.html", {"form": form})
# supprimer un etudiant

def supprimer_etudiant(request, id):

    etudiants = get_object_or_404(Etudiant, id= id)

    etudiants.delete()

    messages.success(request, 'Etudiant supprimer avec succes!')
    

    return redirect("dashboardadmin")


# modifier un etudiant
def modifier_etudiant(request, id):
    etudiant = get_object_or_404(Etudiant, id=id)
    if request.method == 'POST':
            form = EtudiantForm(request.POST, instance=etudiant)
            if form.is_valid():
                form.save()
            messages.success(request, 'Etudiant modifier avec succes!')
            return redirect('dashboardadmin')
    else:

        form = EtudiantForm(instance=etudiant)
    return render(request, 'formulaireadmin.html',{'form':form})




        