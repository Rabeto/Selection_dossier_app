from django.test import TestCase
from faker import Faker
from .models import Candidat

# Create your tests here.

faker = Faker()

for i in range(10):
    nom = faker.first_name()
    prenom = faker.last_name()
    note_HG = faker.random_int(5,19)
    note_ANG = faker.random_int(5,19)
    note_FR = faker.random_int(5,19)
    Candidat.objects.create(Nom = nom, Prenom = prenom, Note_HG = note_HG, Note_ANG = note_ANG, Note_FR = note_FR)