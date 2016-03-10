from django.shortcuts import render
from .models import Course, Create_course
from datetime import datetime
from .models import Course
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

def get_table(request):
    course1 = Course(name='Programming 101 with Python', description='Python!', start_date=datetime(
        day=1, month=1, year=2016), end_date=datetime(day=1, month=3, year=2016))
    course1.save()
    course2 = Course(name='Programming 101 with Ruby', description='Ruby.', start_date=datetime(
        day=10, month=1, year=2016), end_date=datetime(day=1, month=3, year=2016))
    course2.save()
    # courses = Course.objects.all()
    courses = Course.objects.all()
    return render(request, 'index.html', locals())


def python_page(request):

    return render(request, 'Python.html', locals())


def ruby_page(request):

    return render(request, 'Ruby.html', locals())


def new_course_create(request):
    if request.method == 'POST':
        name = request.POST['name']
        # print(request.POST)
        des = request.POST['desc']
        start = request.POST['st_date']
        end = request.POST['end_date']

        new_course = Course(name=name, description=des, start_date=start, end_date=end)
        new_course.save()

        return HttpResponse("Thank you")

    form = Course()
    return render(request, 'create_course.html', locals())


def edit_course(request, lang=None):
    # lang[0] = lang[0].upper()
    # entry = Course.objects.all()
    # print(Course.objects.get(pk=2).name)
    lang = lang[0].upper() + lang[1:]
    # print(lang)
    if request.method == 'POST':
        new_name = request.POST['name']
        new_desc = request.POST['desc']
        new_start = request.POST['st_date']
        new_end = request.POST['end_date']
    
        x = Course.objects.filter(name__contains=lang)
        
        for item in x:
            item.name = new_name
            item.save()
            item.description = new_desc
            item.save()
            item.start_date = new_start
            item.save()
            item.end_date = new_end
            item.save()

        return HttpResponseRedirect(reverse('home'))

    return render(request, 'modify_course.html', locals())