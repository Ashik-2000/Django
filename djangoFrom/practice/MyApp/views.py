from django.shortcuts import render
from .models import MembersData
from .forms import Members

# Create your views here.
def form(req):
    obj = Members()
    if req.method == 'POST':
        name = req.POST.get('name')
        email = req.POST.get('email')
        paid = req.POST.get('paid')
        obj = MembersData.objects.create(name = name, email = email, paid = paid)
        obj.save()
    return render(req, 'form.html', {'obj': obj})