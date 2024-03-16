from django.shortcuts import render
from .models import LearnPlace, Certification


def home(request):
    return render(request, "devel/home.html", {})


def cert(request):
    learn_places = LearnPlace.objects.all()
    SoloLearn = Certification.objects.filter(learnt_from=1)
    GrassHopper = Certification.objects.filter(learnt_from=2)
    classname = Certification.objects.values('classname')
    context = {
        'learn_places': learn_places,
        'SoloLearn': SoloLearn,
        'GrassHopper': GrassHopper,
        'classname': classname,
    }
    return render(request, "devel/cert.html", context)


def cv(request):
    abilities = ['Linux', 'flexibility', 'enthusiastic', 'reliable', 'honest', 'prudent', 'wise', 'clever', 'creative', 'persistent', 'monotony tolerance', 'accurate', 'systematic', 'good team player', 'problem solving skills', 'a constant and fast learner', 'logical mind with great memory', 'keeping up-to-date knowledge', 'management of computer controlled systems', 'scheduled maintenance on my works']
    context = {
        'abilities': abilities,
    }
    return render(request, "devel/cv.html", context)


def devel(request):
    return render(request, "devel/devel.html", {})


def affiliates(request):
    return render(request, "devel/affiliates.html", {})
