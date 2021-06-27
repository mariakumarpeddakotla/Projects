from django.db import models

class Registration(models.Model):
    name = models.CharField(max_length=30)
    contact = models.IntegerField(unique=True)
    email = models.EmailField(max_length=30,unique=True)
    location = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
