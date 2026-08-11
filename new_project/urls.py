from django.urls import path
from .views import *

urlpatterns = [

    
     path("inscrire_etudiant/", inscrire_etudiant , name = 'inscrire_etudiant'),
     path("supprimer_etudiant/<int:id>/", supprimer_etudiant, name='supprimer_etudiant'),
     path("modifier_etudiant/<int:id>/", modifier_etudiant, name='modifier_etudiant'),
     path("liste_professeur/", liste_professeur, name='liste_professeur'),
     path("ajouter_professeur/", ajouter_professeur, name='ajouter_professeur'),
     path("modifier_professeur/<int:id>/", modifier_professeur, name='modifier_professeur'),
     path("supprimer_professeur/<int:id>/", supprimer_professeur, name='supprimer_professeur'),
     
     
     
     # path("ajouter_proffesseur/", ajouter_proffesseur, name='ajouter_proffesseur'),
    

]