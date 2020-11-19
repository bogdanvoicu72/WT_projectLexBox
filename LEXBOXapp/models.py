from django.db import models

# Create your models here.


class CarteIdentitate(models.Model):
    name = models.CharField(max_length=255)
    carte_identitate_img = models.ImageField(upload_to='static/images_upload/CI')