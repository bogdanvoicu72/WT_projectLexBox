from django.db import models

# Create your models here.


class CarteIdentitate(models.Model):
    name = models.CharField(max_length=255)
    carte_identitate_img = models.ImageField(upload_to='static/images_upload/CI')


class Utilizatori(models.Model):
    nume = models.TextField(max_length=50)
    prenume = models.TextField(max_length=50)
    email = models.EmailField(max_length=100)
    parola = models.TextField(max_length=30)