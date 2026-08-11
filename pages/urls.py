from django.urls import path
from .views import *

urlpatterns = [

    path("", connexion,name='connexion'),
    path("dashboardadmin/", dashboardadmin,name="dashboardadmin"),
    path("dashboardteacher/", dashboardteacher,name="dashboardteacher"),
    path("dashboardstudent/", dashboardstudent , name = 'dashboardstudent'),
    path("deconnexion/", deconnexion, name="deconnexion"),
    

]