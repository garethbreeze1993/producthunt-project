from django.urls import path
from . import views

urlpatterns = [
    path('Login',views.login, name='Login'),	
    path('Logout',views.logout, name='Logout'),	
    path('SignUp',views.signup, name='SignUp'),	

]