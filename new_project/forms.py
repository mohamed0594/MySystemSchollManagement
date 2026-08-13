# from dataclasses import fields
# from .models import Professeur
from django import forms
from .models import Etudiant, Professeur,Notes

class EtudiantForm(forms.ModelForm):
    class Meta:
        model = Etudiant
        fields = [
            "nom",
            "prenom",
            "age",
            "classe",
            "matricule",
            "id_user",
        ]


class ProfesseurForm(forms.ModelForm):
    class Meta:
        model = Professeur
        fields = [
            'nom',
            'prenom',
            'age',
            'classe',
            'matiere',
            'id_user',
        ]


class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = [
            'etudiant',
            'matiere',
            'note',
        ]
