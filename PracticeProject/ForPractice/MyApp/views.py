from django.shortcuts import render
from .models import Students
# Create your views here.

def showData(request):
    d = Students.objects.all()
    return render(request, "show.html", {"data" : d})