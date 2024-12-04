from django.shortcuts import render
from .forms import Members

# Create your views here.
def form(req):
    obj = Members()
    if req.method == 'GET':
        name = req.GET.get('name')
        email = req.GET.get('email')
        paid = req.GET.get('paid')
        print(name, email, paid)
    return render(req, 'form.html', {'obj': obj})