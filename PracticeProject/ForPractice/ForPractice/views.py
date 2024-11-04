from django.shortcuts import HttpResponse, render

def show(request, num):
    a = num
    x = "is the square of"
    y = a*a
    return HttpResponse(f"{y} {x} {a}.")

def home(requsest):
    ashik = "Ashik"
    jahangir = "Jahangir"
    nipu = "Nipu"
    context = {
        "a" : ashik,
        "j" : jahangir,
        "n" : nipu
    }
    return render(requsest, "index.html", context)