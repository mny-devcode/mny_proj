from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('', views.home, name='home'),
    path('cert/', views.cert, name='cert'),
    path('cv/', views.cv, name='cv'),
    path('devel/', views.devel, name='devel'),
]

urlpatterns += staticfiles_urlpatterns()
