from django.db import models
from django.contrib.auth.models import User

class Utilisateur(models.Model):
    SEXE_CHOICES = [
        ('F', 'Femme'),
        ('H', 'Homme'),
    ]
    STATUT_CHOICES = [
        ('P', 'Parents'),
        ('A', 'Apprenant'),
    ]
    NIVEAU_CHOICES = [
        ('3EME', '3EME'),
        ('Tle C', 'Tle C'),
        ('Tle D', 'Tle D'),
        ('Tle E', 'Tle E'),
        ('Tle G', 'Tle G'),
        ('Tle A', 'Tle A'),
    ]

    user= models.OneToOneField(User, on_delete=models.CASCADE)
    sexe = models.CharField(max_length=1, choices=SEXE_CHOICES)
    statut = models.CharField(max_length=1, choices=STATUT_CHOICES)
    numero_telephone = models.CharField(max_length=20)
    niveau = models.CharField(max_length=10, choices=NIVEAU_CHOICES)
    etablissement = models.CharField(max_length=100)
    

    def __str__(self):
        return f"{self.user.last_name} {self.user.first_name}"
