from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request, "devel/home.html", {})


def cert(request):
    return render(request, "devel/cert.html", {})


def cv(request):
    return render(request, "devel/cv.html", {})


def devel(request):
    return render(request, "devel/devel.html", {})
