from django.contrib import admin
from .models import Classes, Matieres, Professeur, Etudiant,Notes

# Register your models here.
admin.site.register(Classes)
admin.site.register(Matieres)
admin.site.register(Notes)
admin.site.register(Professeur)
admin.site.register(Etudiant)
