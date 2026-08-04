from django.contrib import messages
from django.shortcuts import render, redirect
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