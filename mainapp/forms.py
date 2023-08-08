# forms.py
from django import forms
from .models import Utilisateur
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

class InscriptionForm(forms.ModelForm):
    class Meta:
        model = Utilisateur
        fields = ['sexe', 'statut', 'numero_telephone', 'niveau', 'etablissement']
        widgets = {
            
            'sexe': forms.Select(attrs={'placeholder': 'Sexe*'}),
            'statut': forms.Select(attrs={'placeholder': 'Vous êtes ?*'}),
            'numero_telephone': forms.TextInput(attrs={'placeholder': 'Numéro de téléphone*'}),
            'niveau': forms.Select(attrs={'placeholder': '[Niveau]*'}),
            'etablissement': forms.TextInput(attrs={'placeholder': 'Etablissement*'}),
        }

class ConnexionForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        wigdets = {}
        for x in fields :
            wigdets[x] = forms.TextInput(attrs={'class':'form-control'})
            


class CreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'first_name', 'last_name']
        wigdets = {}
        for x in fields :
            wigdets[x] = forms.TextInput(attrs={'class':'form-control'})
            
