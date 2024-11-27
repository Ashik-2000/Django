from django.shortcuts import render

# Create your views here.
# Authetication Functions

def signUp(request):
    return render(request, 'signup.html')

def logIn(request):
    return render(request, 'login.html')
