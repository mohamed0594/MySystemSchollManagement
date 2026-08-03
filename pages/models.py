from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Utilisateur(AbstractUser):
    ChoiceRole = (
        ('admin','administrateur'),
        ('enseignant','enseignant' ),
        ('etudiant','etudiant')
    )
    role = models.CharField(
        max_length= 25,
        choices=ChoiceRole,
        default='etudiant'
        
    )
    email = models.EmailField(unique=True)
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name', 'role']
    
    def __str__(self):
        return f"{self.username}-{self.role}-{self.email} "
    
