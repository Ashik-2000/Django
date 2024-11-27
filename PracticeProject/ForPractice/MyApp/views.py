from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from .models import Students
# Create your views here

# Authetication Functions

def signUp(request):
    if request.method == 'POST':
        name = request.POST.get('uname')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        if pass1 == pass2:
            user = User(username = name, email = email)
            user.set_password(pass1)
            user.save()
            return redirect('login')
    return render(request, 'signup.html')

def logIn(request):
    if request.method == 'POST':
        name = request.POST.get('uname')
        password = request.POST.get('password')
        user = authenticate(request, username = name, password = password)
        if user:
            login(request, user)
            return redirect('form')
    return render(request, 'login.html')

def logOut(request):
    logout(request)
    return redirect('login')

# Data Entry Functions

def form(request):
    if request.method == 'POST':
        name = request.POST.get('iname')
        dept = request.POST.get('idept')
        email = request.POST.get('imail')
        phone = request.POST.get('iphone')
        Students.objects.create(name = name, dept = dept, email = email, phone = phone)
    return render(request, 'form.html')

def data(request):
    d = Students.objects.all()
    return render(request, 'data.html', {'data': d})

def deleteData(request, id):
    Students.objects.get(id = id).delete()
    return redirect('data')

def updateData(request, id):
    if request.method == 'POST':
        obj = Students.objects.get(id = id)
        obj.name = request.POST.get('iname')
        obj.dept = request.POST.get('idept')
        obj.email = request.POST.get('imail')
        obj.phone = request.POST.get('iphone')
        obj.save()
        return redirect('data')
    obj = Students.objects.get(id = id)
    return render(request, 'update.html', {'obj':obj})
