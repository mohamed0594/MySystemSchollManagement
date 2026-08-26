from django.urls import path
from .views import *
from pages.views import absences, parametres, parametresteacher, gestion_utilisateurs, modifier_role, supprimer_utilisateur
urlpatterns = [

    
     path("inscrire_etudiant/", inscrire_etudiant , name = 'inscrire_etudiant'),
     path("supprimer_etudiant/<int:id>/", supprimer_etudiant, name='supprimer_etudiant'),
     path("modifier_etudiant/<int:id>/", modifier_etudiant, name='modifier_etudiant'),
     path("liste_professeur/", liste_professeur, name='liste_professeur'),
     path("ajouter_professeur/", ajouter_professeur, name='ajouter_professeur'),
     path("modifier_professeur/<int:id>/", modifier_professeur, name='modifier_professeur'),
     path("supprimer_professeur/<int:id>/", supprimer_professeur, name='supprimer_professeur'),
     path('gestion_notes/', gestion_notes, name='gestion_notes'),
     path('ajouter_note/', ajouter_note, name='ajouter_note'),
     path('modifier_note/<int:note_id>/', modifier_note, name='modifier_note'),
     path('rechercher_notes/', rechercher_notes, name='rechercher_notes'),
     path('ajouter_matiere/', ajouter_matiere, name='ajouter_matiere'),
     path('parametres/',parametres, name='parametres' ),
     path('parametresteacher/',parametresteacher, name='parametresteacher' ),
     path('absences/', absences, name='absences'),
     path('gestion_utilisateurs/', gestion_utilisateurs, name='gestion_utilisateurs'),
     path('modifier_role/<int:id>/', modifier_role, name='modifier_role'),
     path('supprimer_utilisateur/<int:id>/', supprimer_utilisateur, name='supprimer_utilisateur'),

     
     
     
     
     # path("ajouter_proffesseur/", ajouter_proffesseur, name='ajouter_proffesseur'),
    

]