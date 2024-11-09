from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

class Ville(models.Model):
    nomV = models.CharField(max_length=255)  
    nomQ = models.CharField(max_length=255)
    numM = models.TextField(max_length=255)  
    descriptionV = models.TextField() 
    imageQ = models.ImageField(_("imageQuantier"), upload_to='images/quantier/') 
    imageM = models.ImageField(_("imageMaison"), upload_to='images/maisons/')  
    imageCH = models.ImageField(_("imagechambre"), upload_to='images/chambres/') 
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_creation = models.DateTimeField(auto_now_add=True)  
    latitude = models.FloatField(null=True, blank=True)  # Ajout du champ latitude
    longitude = models.FloatField(null=True, blank=True) 

    def __str__(self):
        return self.nomV  



class Client(models.Model):
    nom = models.CharField(max_length=100)  # Nom du client
    prenom = models.CharField(max_length=100)  
    sexe = models.CharField(max_length=100)
    email = models.EmailField(unique=True)  # Email du client, avec contrainte d'unicité
    adresse = models.CharField(max_length=255, null=True, blank=True)  # Adresse du client (optionnelle)
    telephone = models.CharField(max_length=20, null=True, blank=True)  # Numéro de téléphone (optionnel)
    date_inscription = models.DateTimeField(auto_now_add=True)  # Date d'inscription du client
    

    def __str__(self):
        return f"{self.prenom} {self.nom}"


class Visite(models.Model):
    ville = models.ForeignKey(Ville, on_delete=models.CASCADE)  # Relation avec Ville
    client = models.ForeignKey(Client, on_delete=models.CASCADE)  # Relation avec Client
    date_visite = models.DateTimeField()  # Date et heure de la visite
    remarques = models.TextField(null=True, blank=True)  # Optionnel pour des remarques ou commentaires sur la visite

    def __str__(self):
        return f"Visite de {self.client} à {self.ville} le {self.date_visite}"