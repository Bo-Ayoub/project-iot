from rest_framework import serializers
from .models import Utilisateur, Rolee , Actionn,Commentaire,Incident,Temperature

class RoleeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rolee
        fields = '__all__'

class UtilisateurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Utilisateur
        fields = '__all__'
class ActionnSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actionn
        fields = '__all__'
class IncidentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Incident
        fields = '__all__'
class TemperatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Temperature
        fields = '__all__'
class CommentaireSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commentaire
        fields = '__all__'





