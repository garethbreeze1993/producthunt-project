from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

def login(request):
    return render(request, 'accounts/login.html')
	
def logout(request):
    return render(request, 'accounts/signup.html')

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