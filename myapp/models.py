from django.db import models

# Create your models here.
class User(models.Model):
    username=models.CharField(max_length=20,default="")
    email=models.EmailField(max_length=254,default="")
    password1=models.CharField(max_length=50,default="")
    password2=models.CharField(max_length=50,default="")


    

