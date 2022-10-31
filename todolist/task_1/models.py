from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class register1(AbstractUser):
    profile_picture=models.ImageField(null=True,blank=True,upload_to="images/")
    email=models.EmailField(unique=True)

class todo(models.Model):
    Title=models.CharField(unique=True,max_length=100)
    Note=models.TextField()
    Save_Date=models.DateTimeField(auto_now_add=True)
    Last_Date=models.DateTimeField()
    Status=models.BooleanField()
    Count=models.IntegerField(default=0)
    name=models.ForeignKey(register1,on_delete=models.CASCADE)