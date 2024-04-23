from django.shortcuts import render,redirect
from django.contrib.auth.models import User 
from django.contrib.auth.models import auth
from signup.models import *
from django.contrib import messages
# Create your views here


# Create your views here.
def login (request):
    if request.method =='POST':
        username=request.POST['username']
        password =request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('dashboard')
        else:
            messages.info(request,'invalid username or password')
            return redirect('/')
    else:
        return render(request,'log.html')