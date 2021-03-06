"""zhihupaper URL Configuration

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
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from paper import views

urlpatterns = [
    url(r'^$', views.home),
    url(r'^home/$', views.home),
    url(r'^home$', views.home),
    url(r'^story/(\d+)$', views.story),
    url(r'^imgurl/(?P<url>.*)$', views.get_pic),
    url(r'^story/before/(\d+)$', views.ajax_morestory),
    url(r'^story/before/m/(\d+)$', views.m_ajax_morestory),
    url(r'^m/$', views.mobile),
    url(r'^m$', views.mobile),
]
