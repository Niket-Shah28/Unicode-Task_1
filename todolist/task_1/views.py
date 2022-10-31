from django.shortcuts import render,redirect
from .forms import registeration,SignIn,person_list
from django.contrib.auth import login,authenticate,logout
from .models import register1,todo
from django.contrib import messages
from .decoraters import signin_required
# Create your views here.

#This Function checks login details and authenticates and let user login or threow error based on details
@signin_required
def Sign_IN(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('display')
        else:
            messages.error(request,"Invalid Login Details")
            signin=SignIn()
            return render(request,'signin.html',{'signin':signin,'message':messages})
    else:
        signin=SignIn()
        return render(request,'signin.html',{'signin':signin})

#This function checks the registeration details and will not save if requirements are not met properly
def signup(request):
    if request.method=="POST":
        register=registeration(request.POST,request.FILES)
        if register.is_valid():
            register.save()
            return redirect('login')
        else:
            messages.error(request,"Invalid Details")  
            return render(request,'register.html',{'register':register})
    else:
        register=registeration()
        return render(request,'register.html',{'register':register})

#This is How Welcome page look
def display_page(request):
    if request.method=="POST":
        return redirect('list')
    else:
        Name2=request.user
        obj=todo.objects.filter(name=Name2)
        return render(request,'welcome.html',{'Name':Name2,'obj':obj})

#This def just takes the input for list and redirects to home page 
def list(request):
    if request.method=="POST":
      f3=person_list(request.POST)
      if f3.is_valid():
            Data=todo()
            Data.Title=f3.cleaned_data['Title']
            Data.Note=f3.cleaned_data['Note']
            Data.Last_Date=f3.cleaned_data['Last_Date']
            Data.Count=f3.cleaned_data['Count'] 
            Data.Status=f3.cleaned_data['Status']
            Data.name=request.user 
            Data.save()
            return redirect('display')
      else:
            f3=person_list()
            return render(request,'list.html',{'list':f3})

    else:
        f3=person_list()
        return render(request,'list.html',{'list':f3})

#This def logs out from server
def signout(request):
    logout(request)
    return redirect('login')

#This Updates the data if needed
def update(request,id):
    if request.method=="POST":
        pi=todo.objects.get(pk=id)
        f3=person_list(request.POST,instance=pi)
        if f3.is_valid():
            Data=todo.objects.get(pk=id)
            Data.Title=f3.cleaned_data['Title']
            Data.Note=f3.cleaned_data['Note']
            Data.Last_Date=f3.cleaned_data['Last_Date']
            Data.Count=f3.cleaned_data['Count'] 
            Data.Status=f3.cleaned_data['Status']
            Data.name=request.user 
            Data.save()
            return redirect('display')
    else:
        pi=todo.objects.get(pk=id)
        f3=person_list(instance=pi)
        return render(request,'update.html',{'list':f3,'id':pi})

#This one gets the Instance and deletes that list and returns back to display page
def delete(request,id):
    if request.method=="POST":
        pi=todo.objects.get(pk=id)
        pi.delete()
        return redirect('display')

#This Function is to just see your profile
def viewprofile(request):
    name=request.user
    profile_data=register1.objects.get(username=name)
    return render(request,'profile.html',{'profile':profile_data})

