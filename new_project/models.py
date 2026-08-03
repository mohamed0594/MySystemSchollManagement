from django.db import models
from pages.models import Utilisateur


# Create your models here.


class Matieres (models.Model):
    nom=models.CharField(max_length=50)

    class Meta:
        verbose_name = "Matière"
        verbose_name_plural = "Matières"

    def __str__(self):
        return self.nom
    


class Classes (models.Model):
    nom=models.CharField(max_length=50)

    class Meta:
        verbose_name = "Classe"
        verbose_name_plural = "Classes"
class Classes (models.Model):
    nom=models.CharField(max_length=50)

    def __str__(self):
        return self.nom
    


class Etudiant (models.Model):
    nom=models.CharField(max_length=100)
    prenom =models.CharField(max_length=100)
    age=models.IntegerField(default=0)
    classe = models.ForeignKey(Classes, on_delete=models.SET_NULL,null=True)
    matricule =models.CharField(max_length=50, unique=True)
    id_user =models.OneToOneField(Utilisateur, on_delete=models.CASCADE, related_name='etudiant' , null=True)

    class Meta:
        verbose_name = "Etudiant"
        verbose_name_plural = "Etudiants"

    def __str__(self):
        return f"{self.nom} - {self.prenom} - {self.classe} - {self.matricule}"




class Professeur (models.Model):
    nom=models.CharField(max_length=100)
    prenom =models.CharField(max_length=100)
    age=models.IntegerField(default=0)
    classe = models.ForeignKey(Classes, on_delete=models.SET_NULL,null=True,blank=True)
    matiere =models.ForeignKey (Matieres, on_delete=models.SET_NULL,null=True, blank=True)
    id_user =models.OneToOneField(Utilisateur, on_delete=models.CASCADE, related_name='professeur' , null=True )

    class Meta:
        verbose_name = "Professeur"
        verbose_name_plural = "Professeurs"

    def __str__(self):
        return f"{self.nom} - {self.matiere} - {self.classe}"