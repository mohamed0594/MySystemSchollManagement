from django.contrib import admin
from .models import Classse, Matiere, Notes, Enseignant, Etudiant

# Register your models here.
admin.site.register(Classse)
admin.site.register(Matiere)
admin.site.register(Notes)
admin.site.register(Enseignant)
admin.site.register(Etudiant)
