from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from .models import *
from .serializers import *

class UtilisateurViewSet(viewsets.ModelViewSet):
    queryset = Utilisateur.objects.all()
    serializer_class = UtilisateurSerializer

class DemandeVidageViewSet(viewsets.ModelViewSet):
    queryset = DemandeVidage.objects.all()
    serializer_class = DemandeVidageSerializer

class DemandeLavageViewSet(viewsets.ModelViewSet):
    queryset = DemandeLavage.objects.all()
    serializer_class = DemandeLavageSerializer

class DemandePuisageViewSet(viewsets.ModelViewSet):
    queryset = DemandePuisage.objects.all()
    serializer_class = DemandePuisageSerializer
