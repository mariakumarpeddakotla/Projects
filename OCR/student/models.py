from django.db import models

class Student_RegistrationModel(models.Model):
    name = models.CharField(max_length=30,null=False)
    contact = models.IntegerField(unique=True,null=False)
    email = models.EmailField(max_length=30,unique=True,null=False)
    password = models.CharField(max_length=30,null=False)
    otp = models.IntegerField(default=000000,null=False)
    status = models.CharField(max_length=30,null=False,default='pending')
    date_time = models.DateTimeField(auto_now_add=True)
