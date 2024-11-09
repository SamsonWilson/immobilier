from django import forms
from .models import Ville, Client

class VilleForm(forms.ModelForm):
    class Meta:
        model = Ville
        fields = ["nomV","nomQ","numM", "descriptionV", "imageQ","imageM","imageCH","user"]

class clientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['nom', 'prenom', 'email', 'adresse','telephone', 'sexe', ]       
