from .models import UserProfile
from django.contrib.auth.models import User,auth
from django.shortcuts import render,redirect
from django.contrib import messages

def signup(request):
    if request.method == 'POST':
        # Extracting form data
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        profession = request.POST.get('profession')
        street_address = request.POST.get('street_address')
        city = request.POST.get('city')
        country = request.POST.get('country')
        zip_code = request.POST.get('zip_code')
         
        if User.objects.filter(username=username).exists():
            messages.info(request,'Username taken')
            return redirect('signup')    
        elif User.objects.filter(email=email).exists():
            messages.info(request,'email exists')
            return redirect('signup')
        # Create a new user instance
        else: 
            user = User.objects.create_user(username=username, password=password, email=email)
        
        # Create a profile for the user
        profile = UserProfile(user=user, profession=profession, street_address=street_address, city=city, country=country, zip_code=zip_code)
        profile.save()
        
        # Redirect the user to the dashboard
        return redirect('login')
    else:
        return render(request, 'signup.html')