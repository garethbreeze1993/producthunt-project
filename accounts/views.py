from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'],password = request.POST['password']) # creates a user object if there is a valid user with that username and password in the system
        if user is not None:
            auth.login(request,user) # if a user object is created above login that person
            return redirect('home')
        else:
            return render(request, 'accounts/login.html',{'error':'No matches for that Username and/or Password','user':user})		
    else:
        return render(request, 'accounts/login.html')
	
def logout(request):
    if request.method == 'POST':
        auth.logout(request)# logs person out 
        return redirect('home')		
    

def signup(request):
    if request.method == 'POST':
        #User has entered info and wants an account
        if request.POST['password1'] ==	request.POST['password2']:
            try:		
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'accounts/signup.html', {'error':'Username already exists'})		
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'], password = request.POST['password1'])
                auth.login(request,user)
                return redirect('home')	
        else:
            return render(request, 'accounts/signup.html', {'error':'Your passwords do not match'})		            		
    else:
        # User wants to enter info in order to sign up	
        return render(request, 'accounts/signup.html')	