from django.shortcuts import render, redirect
from .models import Students
# Create your views here.

def showData(request):
    d = Students.objects.all()
    return render(request, "show.html", {"data" : d})

def formData(request):
    if request.method=="POST":
        pname = request.POST.get('pname')
        pdpt = request.POST.get('pdpt')
        pemail = request.POST.get('pmail')
        pnumber = request.POST.get('pnumber')
        Students.objects.create(name=pname, dept=pdpt, email=pemail, phone=pnumber)
    return render(request, 'form.html')

def deleteData(request,pk):
    Students.objects.get(id=pk).delete()
    return redirect('showData')

def updateData(request,id):
    if request.method=="POST":
        pname = request.POST.get('pname')
        pdpt = request.POST.get('pdpt')
        pemail = request.POST.get('pmail')
        pnumber = request.POST.get('pnumber')
        Students(id = id,  name=pname, dept=pdpt, email=pemail, phone=pnumber).save()
        return redirect('showData')
    obj = Students.objects.get(id = id)
    return render(request, 'form1.html', {"obj":obj})