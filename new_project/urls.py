from django.urls import path
from .views import *

urlpatterns = [

    
     path("inscrire_etudiant/", inscrire_etudiant , name = 'inscrire_etudiant'),
     path("supprimer_etudiant/<int:id>/", supprimer_etudiant, name='supprimer_etudiant'),
     path("modifier_etudiant/<int:id>/", modifier_etudiant, name='modifier_etudiant')
    

]