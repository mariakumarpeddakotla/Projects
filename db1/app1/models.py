from django.db import models

class Register(models.Model):

    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    uname = models.CharField(max_length=30,unique=True)
    password = models.CharField(max_length=30,unique=True)
    repass = models.CharField(max_length=30)
    age = models.IntegerField()
