from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^posts/$', views.post_list,name='list'),
    url(r'^posts/(?P<slug>[\w-]+)/$', views.post_detail, name='detail'),

]