from django.db import models

# Create your models here.


class Employee(models.Model):
    e_name = models.CharField(max_length=50)
    e_age = models.IntegerField()
    e_sal = models.FloatField()
    e_add = models.CharField(max_length=50)
