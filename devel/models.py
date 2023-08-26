from django.db import models

# Create your models here.

class LearnPlace(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.name


class Certification(models.Model):
    learnt_from = models.ForeignKey(LearnPlace, on_delete=models.SET_NULL, null=True, blank=True)
#    learnt_from = models.CharField(max_length=50, null=False, blank=False)
    image = models.ImageField(null=False, blank=False)
    description = models.CharField(max_length=100, null=False, blank=False)
    classname = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
#        return self.learnt_from
        return self.description
