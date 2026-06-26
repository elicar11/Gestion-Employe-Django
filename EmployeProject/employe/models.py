from django.db import models

class Employe(models.Model):
    matricule     = models.CharField(max_length=50)
    nom           = models.CharField(max_length=255)
    email         = models.EmailField()
    poste         = models.CharField(max_length=100)
    salaire       = models.DecimalField(max_digits=10, decimal_places=2)
    dateNaissance = models.DateField()
    numero        = models.IntegerField()
    
    def __str__(self):
        return self.nom