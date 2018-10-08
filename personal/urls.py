from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^education/$', views.education, name='education'),
    url(r'^projects/$', views.projects, name='projects'),
    url(r'^skills/$', views.skills, name='skills'),
    url(r'^design/$', views.design, name='design'),
    url(r'^hobby_zone/$', views.hobby_zone, name='hobby_zone'),
]