from django.conf.urls import include, url

from .views import get_table


urlpatterns = [
  # url(r'^$', home, name='home'),
  url(r'^$', 'courses.views.get_table', name='home'),
  url(r'^course/python/$', 'courses.views.python_page', name = 'python'),
  url(r'^course/ruby/$', 'courses.views.ruby_page', name = 'ruby'),
  url(r'^course/new/$', 'courses.views.new_course_create', name = 'create'),

]