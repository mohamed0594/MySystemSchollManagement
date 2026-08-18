
from django import forms
from django.contrib.auth.forms import PasswordChangeForm
from django.forms.widgets import PasswordInput
from .models import Utilisateur

# FORMULAIRE DE CONNEXION
class Utilisateurforms(forms.Form):
    username = forms.CharField(
        label="Non d'utlisateur",
        widget= forms.TextInput (attrs={
            
            'placeholder': 'Username'
        })

           )

    password = forms.CharField(
        label="Mot de Passe",
        widget= forms.PasswordInput(attrs={
            'placeholder' :'Password'
        })
    )
# FORMULAIRE DES INFORMATIONS PERSONNELLES

class UtilisateurInfoForm(forms.ModelForm):

    class Meta:
        model = Utilisateur

        fields = [
            'first_name',
            'last_name',
            'email',
        ]
        widgets = {
            'first_name':forms.TextInput(attrs={
                'placeholder': 'Veuillez entrer votre nom '

            }
            ),
            'last_name':forms.TextInput(attrs={
                'placeholder':'Veuillez entrer prenom '
            }
            ),
            'email': forms.EmailInput(attrs={
                'placeholder':'Veuillez entrer votre email'
            })
        }
# formulaire mot de passe
class ModifierMotDePasseForm(PasswordChangeForm):

    ancienPassword = forms.CharField(
        label="Entrer l'ancien mot de passe",
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Ancien mot de passe'
            }
        )
    )

    new_password = forms.CharField(
        label="Entrer le nouveau mot de passe",
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Nouveau mot de passe'
            }
        )
    )

    confirmation = forms.CharField(
        label="Confirmer le nouveau mot de passe",
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Confirmation du nouveau mot de passe'
            }
        )
    )
    # fonction pour verifier la veracité du mot de passe


    # def effacer(self):
    #     cleaned_data = super().effacer()
    #     new_password = cleaned_data.get(
    #         "Nouveau mot de Passe"
    #     )

    #     confirmation = cleaned_data.get(
    #         "Confirmation mot de passe"
    #     )

    #     if new_password and confirmation:

    #         if confirmation!= new_password:

    #             raise forms.ValidationError(
    #                 "Les deux nouveaux mots de passe ne correspondent pas."
    #             )
    #     return cleaned_data
