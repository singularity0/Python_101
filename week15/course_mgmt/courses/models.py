
from django.db import models
from django.forms import ModelForm
from datetime import datetime, date, timedelta


# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length = 140, null=False)
    description = models.CharField(max_length = 140)
    start_date = models.DateField(help_text="format: YYYY-MM-DD")
    end_date = models.DateField(help_text="format: YYYY-MM-DD")
    # duration = models.DateTimeField(end_date - start_date).months


    # def __str__(self):
    #     return self.description

    # def __init__(self, name, description, start_date, end_date):
    #     self.name = name
    #     self.description = description
    #     self.start_date = start_date
    #     self.end_date = end_date

    def duration(self):
        delta = ((self.end_date) - (self.start_date))
        result = round(delta.days / 30)
        return result


class Create_course(ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'description', 'start_date', 'end_date']


