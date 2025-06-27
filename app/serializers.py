from rest_framework import serializers
from .models import Utilisateur, DemandeVidage, DemandeLavage, DemandePuisage

class UtilisateurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Utilisateur
        fields = '__all__'

class DemandeVidageSerializer(serializers.ModelSerializer):
    class Meta:
        model = DemandeVidage
        fields = '__all__'

class DemandeLavageSerializer(serializers.ModelSerializer):
    class Meta:
        model = DemandeLavage
        fields = '__all__'

class DemandePuisageSerializer(serializers.ModelSerializer):
    class Meta:
        model = DemandePuisage
        fields = '__all__'
