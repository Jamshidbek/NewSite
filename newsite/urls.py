"""newsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^$', views.index, name='index'),

    url(r'^$', views.region_list, name='region_list'),
    url(r'^region/(?P<pk>\d+)/$', views.region_detail, name='region_detail'),
    url(r'^region/new/$', views.region_new, name='region_new'),
    url(r'^region/(?P<pk>\d+)/edit/$', views.region_edit, name='region_edit'),

    url(r'^region/(?P<pk>\d+)/district/$', views.district_list, name='district_list'),
    url(r'^district/(?P<pk>\d+)/$', views.district_detail, name='district_detail'),
    url(r'^district/(?P<pk>\d+)/new/$', views.district_new, name='district_new'),
    url(r'^district/(?P<pk>\d+)/edit/$', views.district_edit, name='district_edit'),
]
