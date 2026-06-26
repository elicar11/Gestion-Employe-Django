from django import forms
from .models import Employe

class EmployeForm(forms.ModelForm):
    class Meta:
        model = Employe
        fields = ['matricule', 'nom', 'email', 'poste', 'salaire', 'dateNaissance', 'numero']
        widgets = {
            'matricule' : forms.TextInput(attrs={
                'class' : 'input w-full',
                'placeholder' : 'Matricule'
            }),
            'nom' : forms.TextInput(attrs={
                'class' : 'input w-full',
                'placeholder' : 'Nom'
            }),
            'email' : forms.TextInput(attrs={
                'class' : 'input w-full',
                'placeholder' : 'Email'
            }),
            'poste' : forms.TextInput(attrs={
                'class' : 'input w-full',
                'placeholder' : 'Poste'
            }),
            'salaire' : forms.TextInput(attrs={
                'class' : 'input w-full',
                'placeholder' : 'Salaire'
            }),
            'dateNaissance' : forms.TextInput(attrs={
                'class' : 'input w-full',
                'type' : 'date',
                'placeholder' : 'Date de Naissance'
            }),
            'numero' : forms.TextInput(attrs={
                'class' : 'input w-full',
                'placeholder' : 'Numéro'
            })
        }