from django.db import models

# Create your models here.

from django.db import models

class Utilisateur(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    ville = models.CharField(max_length=100)
    quartier = models.CharField(max_length=100)
    numero_tel = models.CharField(max_length=20)
    mot_de_passe = models.CharField(max_length=128)
    date_inscription = models.DateTimeField(auto_now_add=True)

class DemandeBase(models.Model):
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    date_demande = models.DateTimeField(auto_now_add=True)
    statut = models.CharField(max_length=20, default="en attente")

    class Meta:
        abstract = True

class DemandeVidage(DemandeBase):
    pass

class DemandeLavage(DemandeBase):
    pass

class DemandePuisage(DemandeBase):
    pass
