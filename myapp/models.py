

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Actionn(models.Model):
    dateaction = models.DateTimeField(db_column='dateAction', blank=True, null=True)  # Field name made lowercase.
    descriptionaction = models.CharField(db_column='descriptionAction', max_length=200, blank=True, null=True)  # Field name made lowercase.
    iduser = models.ForeignKey('Utilisateur', models.DO_NOTHING, db_column='idUser', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'actionn'


class Commentaire(models.Model):
    iduser = models.ForeignKey('Utilisateur', models.DO_NOTHING, db_column='idUser', blank=True, null=True)  # Field name made lowercase.
    idincident = models.ForeignKey('Incident', models.DO_NOTHING, db_column='idIncident', blank=True, null=True)  # Field name made lowercase.
    contenue = models.TextField(blank=True, null=True)
    datecommentaire = models.DateTimeField(db_column='dateCommentaire', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'commentaire'


class Incident(models.Model):
    dateincident = models.DateTimeField(db_column='dateIncident', blank=True, null=True)  # Field name made lowercase.
    dateresolution = models.DateTimeField(db_column='dateResolution', blank=True, null=True)  # Field name made lowercase.
    statusresolved = models.TextField(db_column='statusResolved', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    iduser = models.ForeignKey('Utilisateur', models.DO_NOTHING, db_column='idUser', blank=True, null=True)  # Field name made lowercase.
    idtemp = models.ForeignKey('Temperature', models.DO_NOTHING, db_column='idTemp', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'incident'


class Rolee(models.Model):
    libelle = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rolee'


class Temperature(models.Model):
    temprecord = models.FloatField(db_column='tempRecord', blank=True, null=True)  # Field name made lowercase.
    humidityrecord = models.FloatField(db_column='humidityRecord', blank=True, null=True)  # Field name made lowercase.
    daterecord = models.DateTimeField(db_column='dateRecord', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'temperature'


class Utilisateur(models.Model):
    nom = models.CharField(max_length=30, blank=True, null=True)
    prenom = models.CharField(max_length=30, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    mdp = models.CharField(max_length=30, blank=True, null=True)
    apikey = models.CharField(db_column='apiKey', max_length=100, blank=True, null=True)  # Field name made lowercase.
    idrole = models.ForeignKey(Rolee, models.DO_NOTHING, db_column='idRole', blank=True, null=True)  # Field name made lowercase.
    phonenumber = models.TextField(db_column='phoneNumber', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'utilisateur'
