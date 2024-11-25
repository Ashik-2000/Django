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
        obj = Students.objects.get(id = id)
        obj.name = request.POST.get('iname')
        obj.dpt = request.POST.get('idpt')
        obj.email = request.POST.get('imail')
        obj.phone = request.POST.get('iphone')
        obj.save()
        return redirect('showData')
    obj = Students.objects.get(id = id)
    return render(request, 'update.html', {'obj':obj})