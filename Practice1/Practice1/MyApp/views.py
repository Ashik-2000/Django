from django.shortcuts import render, redirect
from .models import Students

# Create your views here.
def form(request):
    if request.method == "POST":
        name = request.POST.get('iname')
        dpt = request.POST.get('idpt')
        email = request.POST.get('imail')
        phone = request.POST.get('iphone')
        Students.objects.create(name=name, dpt = dpt, email = email, phone = phone)
    return render(request, 'form.html')

def showData(request):
    d = Students.objects.all()
    return render(request, 'data.html', {'data' : d})

def deleteData(request, id):
    Students.objects.get(id = id).delete()
    return redirect('showData')

def updateData(request, id):
    if request.method == "POST":
        name = request.POST.get('iname')
        dpt = request.POST.get('idpt')
        email = request.POST.get('imail')
        phone = request.POST.get('iphone')
        Students(id = id, name=name, dpt = dpt, email = email, phone = phone).save()
    return redirect('showData')