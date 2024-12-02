from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate

# Create your views here.
def logIn(req):
    if req.method == "POST":
        name = req.POST.get('name')
        password = req.POST.get('password')
        user = authenticate(username = name, password = password)
        if user:
            login(req, user)
            return redirect('home')
    return render(req, 'login.html')

def home(req):
    return render(req, 'index.html')