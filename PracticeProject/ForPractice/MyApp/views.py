from django.shortcuts import render
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