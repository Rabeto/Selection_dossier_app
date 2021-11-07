from django.db import models
import joblib
import numpy as np
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier

# Create your models here.
class Candidat(models.Model):
    Nom = models.CharField(max_length=50)
    Prenom = models.CharField(max_length=50)
    Note_HG = models.IntegerField(null=True)
    Note_ANG = models.IntegerField(null=True)
    Note_FR = models.IntegerField(null=True)
    Result = models.CharField(max_length=30, blank=True)

    def save(self, *args, **kwargs):
        ml_model = joblib.load('ML/model/ML_KNeighborsModel-1.joblib')
        resultat = np.around(ml_model.predict([[self.Note_HG, self.Note_ANG, self.Note_FR]]))
        if resultat == 0:
            self.Result = "Non Sélectionner"
        else:
            self.Result = "Sélectionner"
        return super().save(*args, *kwargs)

    def __str__(self):
        return self.Nom

        

