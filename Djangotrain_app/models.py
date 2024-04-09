from django.db import models

# Create your models here.

class Trains (models.Model) :

    trainId = models.AutoField(primary_key= True)
    name = models.CharField(max_length = 50)
    destination = models.CharField(max_length = 50)
    overview = models.CharField(max_length = 200)
    time = models.TimeField(max_length=200)
    imagi=  models.ImageField(upload_to='static/img')
    ligne = models.IntegerField()

