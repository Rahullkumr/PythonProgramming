from django.db import models

# Create your models here.


class MovieMod(models.Model):
    mname = models.CharField(max_length=20)
    rdate = models.DateField()
    hero = models.CharField(max_length=50)
    heroine = models.CharField(max_length=50)
    director = models.CharField()
    lang = models.CharField(max_length=20)
    rating = models.FloatField()
