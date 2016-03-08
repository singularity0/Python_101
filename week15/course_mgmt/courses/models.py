from django.db import models
from datetime import datetime, date

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length = 140, null=False)
    description = models.CharField(max_length = 140)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    # duration = models.DateTimeField(end_date - start_date).months


    # def __str__(self):
    #     return self.description
    def __init__(self, name, description, start_date, end_date):
        self.name = name
        self.description = description
        self.start_date = start_date
        self.end_date = end_date

    def duration(self):
        delta = ((self.end_date) - (self.start_date))
        result = round(delta.days / 30)
        return result

course1 = Course(name='Programming 101 with Python', description='Python!', start_date=datetime(day=1,month=1,year=2016) , end_date=datetime(day=1,month=3,year=2016))
course2 = Course(name='Programming 101 with Ruby', description='Ruby.', start_date=datetime(day=10,month=1,year=2016) , end_date=datetime(day=1,month=3,year=2016))