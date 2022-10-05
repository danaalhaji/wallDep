from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *

from datetime import datetime
import bcrypt 

def homePage(request):
    return render(request,"home.html")

def SignUp(request):
    return render(request, "signUp.html")

def signUpSucess(request):
    errors = Users.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key,value in errors.items():
            messages.error(request,value,key)
        return redirect('/signup')
    else:
        firstname = request.POST['firstName']
        lastname = request.POST['LastName']
        Email = request.POST['email']
        passwordAdd = request.POST['Pass']
        pw_hash = bcrypt.hashpw(passwordAdd.encode(), bcrypt.gensalt()).decode()
        user = Users.objects.create(first_name=firstname, last_name = lastname, email=Email, password = pw_hash)
        user.save()
        return render(request,'signUpSuccess.html')

def Login(request):
    return render(request,"login.html")

def loginSuccess(request):
    user = Users.objects.filter(email=request.POST['userEmail'])
    if user: 
        logged_user = user[0] 
        if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
            request.session['username'] = logged_user.first_name
            return render(request,"loginSuccess.html")
    return redirect("/login")


def logOutt(request):
    request.session['username'] = ""
    return redirect("/")

# Create your views here.
