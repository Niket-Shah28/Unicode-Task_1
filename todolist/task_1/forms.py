from django import forms 
from .models import register1,todo
from django.contrib.auth.forms import UserCreationForm

class SignIn(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)
class registeration(UserCreationForm):
    class Meta:
        model=register1
        fields=['username','first_name','last_name','email','profile_picture']

class person_list(forms.ModelForm):
    class Meta:
        model=todo
        fields=["Title","Note","Last_Date","Status","Count"]


