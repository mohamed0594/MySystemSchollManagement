

from django import forms
from .models import Utilisateur

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
