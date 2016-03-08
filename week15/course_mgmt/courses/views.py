from django.shortcuts import render
from .models import Course
from datetime import datetime
from django.template import RequestContext
# Create your views here.

course1 = Course(name='Programming 101 with Python', description='Python!', start_date=datetime(day=1,month=1,year=2016) , end_date=datetime(day=1,month=3,year=2016))
course2 = Course(name='Programming 101 with Ruby', description='Ruby.', start_date=datetime(day=10,month=1,year=2016) , end_date=datetime(day=1,month=3,year=2016))

def get_table(request):
    courses = [course1, course2]
    return render(request, 'index.html',locals())


def python_page(request):

    return render(request, 'Python.html', locals())


def ruby_page(request):

    return render(request, 'Ruby.html', locals())

def new_course_create(request):

    return render(request, 'create_course.html', locals())