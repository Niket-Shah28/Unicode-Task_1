from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,AbstractUser
from django.core.exceptions import ValidationError
# Create your models here.

"""class register(AbstractBaseUser,PermissionsMixin):
    username=models.CharField(max_length=100,unique=True)
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    password=models.CharField(max_length=100)
    confirm_password=models.CharField(max_length=100)
    def clean(self):
        cleaned_data=super().clean()
        valpwd=cleaned_data['password']
        valprwd=cleaned_data['confirm_password']
        if valpwd!=valprwd:
            raise ValidationError("Password does not match")
    email=models.EmailField(unique=True)
    profile_picture=models.ImageField(default=f'<img src="default_image/Presentation2.jpg">')
    EMAIL_FIELD='email' """

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