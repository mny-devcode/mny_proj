from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('', views.home, name='home'),
    path('devel/', views.devel, name='devel'),
    path('cv/', views.cv, name='cv'),
    path('cert/', views.cert, name='cert'),
    path('affiliates/', views.affiliates, name='affiliates'),
]

urlpatterns += staticfiles_urlpatterns()
