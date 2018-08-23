from django.shortcuts import render

def login(request):
    return render(request, 'accounts/login.html')
	
def logout(request):
    return render(request, 'accounts/signup.html')

def signup(request):
    return render(request, 'accounts/signup.html')	