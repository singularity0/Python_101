from django.db import models

# Create your models here.
class Lecture(models.Model):
    uid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length = 140)
    week = models.IntegerField()
    url = models.CharField(max_length = 200)
