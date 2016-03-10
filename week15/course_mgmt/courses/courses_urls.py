from django.conf.urls import url

from .views import get_table, python_page, ruby_page, new_course_create, edit_course


urlpatterns = [
    url(r'^python/$', 'courses.views.python_page', name='python'),
    url(r'^ruby/$', 'courses.views.ruby_page', name='ruby'),
    url(r'^new/$', 'courses.views.new_course_create', name='create'),
    url(r'^edit/(?P<lang>[A-z]{1,20})/$', 'courses.views.edit_course', name='edit')

]
