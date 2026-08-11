# from dataclasses import fields
# from .models import Professeur
from django import forms
from .models import Etudiant, Professeur

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

# class ProfesseurForm(forms.ModelForm):
#     class Meta:
#         model = Professeur
#         fields = [
#             'nom',
#             'prenom',
#             'age',
#             'classe',
#             'matiere',
#             'id_user',
#         ]

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