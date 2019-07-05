from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

class IdClient(models.Model):
    nom = models.CharField(max_length=150)
    prenom = models.CharField(max_length=150)
    dateNaissance = models.DateField()
    password = models.CharField(max_length=50)
    email = models.EmailField()
    question_1 = models.TextField()
    question_2 = models.TextField()
    question_3 = models.TextField()
    telephone = PhoneNumberField(blank=True)




    def __str__(self):
        return self.nom + ' ' +  self.prenom