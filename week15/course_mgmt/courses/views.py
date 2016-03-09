from django.shortcuts import render
from .models import Course, Create_course
from datetime import datetime
# from django.template import RequestContext
from .models import Course
# from django.contrib import messages
# from django import forms
from django.http import HttpResponse



def get_table(request):
    course1 = Course(name='Programming 101 with Python', description='Python!', start_date=datetime(day=1,month=1,year=2016) , end_date=datetime(day=1,month=3,year=2016))
    course1.save()
    course2 = Course(name='Programming 101 with Ruby', description='Ruby.', start_date=datetime(day=10,month=1,year=2016) , end_date=datetime(day=1,month=3,year=2016))
    course2.save()
    courses = [course1, course2]
    return render(request, 'index.html',locals())


def python_page(request):

    return render(request, 'Python.html', locals())


def ruby_page(request):

    return render(request, 'Ruby.html', locals())

def new_course_create(request):
    if request.method == 'POST':
            form = Create_course(request.POST)
            
            if form.is_valid():
            # if form:
                form.save()
                return HttpResponse("Thank you")
                # return render(request, 'thank_you.html')
                # return HttpResponseRedirect(reverse('app_name:url'))
            else:
                # new_course_create()
                return HttpResponse("Form Not Valid {}".format(form['description']))
                # return messages.error(request, "Error")

    
    form = Create_course()
    return render(request, 'create_course.html', {'form':form})

# def new_course_save(request):
#     if request.method == 'POST':
#         form = Course(request.POST)
#         form.save()
#         if form.is_valid():
#             return render(request, 'thank_you.html')
#         else:
#             new_course_create()

