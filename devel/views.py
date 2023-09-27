from django.shortcuts import render
from .models import LearnPlace, Certification
# from .models import Certification

# Create your views here.
def home(request):
    return render(request, "devel/home.html", {})


def cert(request):
    learn_places = LearnPlace.objects.all()
    SoloLearn = Certification.objects.filter(learnt_from=1)
    GrassHopper = Certification.objects.filter(learnt_from=2)
    classname = Certification.objects.values('classname')
#    certifications = Certification.objects.all()
    context = {
        'learn_places': learn_places,
        'SoloLearn': SoloLearn,
        'GrassHopper': GrassHopper,
        'classname': classname,
#        'certifications': certifications
    }
    return render(request, "devel/cert.html", context)


def cv(request):
    return render(request, "devel/cv.html", {})


def devel(request):
    return render(request, "devel/devel.html", {})

def affiliates(request):
    return render(request, "devel/affiliates.html", {})
