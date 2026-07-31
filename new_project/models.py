from django.db import models




class Classse(models.Model):
    nom = models.CharField(max_length=30)
    niveau = models.CharField(max_length=30)
    class Meta:
        verbose_name_plural = "Classes"
        verbose_name = "Classe"

    def __str__(self):
        return self.nom


class Matiere(models.Model):
    nom = models.CharField(max_length=30)

    enseignant = models.ForeignKey(
        'Enseignant',
        on_delete=models.CASCADE
    )
    class Meta:
        verbose_name_plural = "Matieres"
        verbose_name = "Matiere"

    def __str__(self):
        return self.nom


class Notes(models.Model):
    note = models.FloatField()

    matiere = models.ForeignKey(
        'Matiere',
        on_delete=models.CASCADE
    )

    etudiant = models.ForeignKey(
        'Etudiant',
        on_delete=models.CASCADE
    )
    class Meta:
        verbose_name_plural = "Notes"
        verbose_name = "Note"

    def __str__(self):
        return str(self.note)


class Enseignant(models.Model):
    sexe_choices = (
        ('M', 'Masculin'),
        ('F', 'Feminin'),
    )

    nom = models.CharField(max_length=100)

    prenom = models.CharField(max_length=100)

    date_naissance = models.DateField( auto_now_add=False, null=True, blank=True)

    contact = models.CharField(max_length=100, unique=True, null=True, blank=True)

    sexe = models.CharField(max_length=1, choices=sexe_choices)


    class Meta:
        verbose_name_plural = "Enseignants"
        verbose_name = "Enseignant"

    def __str__(self):
        return f"{self.nom} {self.prenom}"


class Etudiant(models.Model):

    choicesSexe = (
        ('M','Masculin'),
        ('F','Feminin')
    )
    nom = models.CharField( max_length=100)
    
    prenom = models.CharField( max_length=100)

    classe = models.ForeignKey( Classse,  on_delete=models.CASCADE)

    date_naissance = models.DateField( auto_now_add=False, null=True, blank=True)

    matricule = models.CharField( max_length=30, unique=True)

    sexe = models.CharField( max_length=1, choices=choicesSexe )
    class Meta:
        verbose_name_plural = "Etudiants"
        verbose_name = "Etudiant"


    def __str__(self):
        return f"{self.nom} {self.prenom}"
    