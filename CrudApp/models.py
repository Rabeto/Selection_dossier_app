from django.db import models

# Create your models here.
class Candidat(models.Model):
    Nom = models.CharField(max_length=50)
    Prenom = models.CharField(max_length=50)
    Note_HG = models.IntegerField()
    Note_ANG = models.IntegerField()
    Note_FR = models.IntegerField()

    def __str__(self):
        return self.Nom

