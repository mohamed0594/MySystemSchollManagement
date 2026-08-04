from django.urls import path
from .views import *

urlpatterns = [

    
     path("inscrire_etudiant/", inscrire_etudiant , name = 'inscrire_etudiant'),
    

]