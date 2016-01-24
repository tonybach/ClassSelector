from django.conf.urls import patterns, url
from class_selector import views

urlpatterns = patterns('', 
        url(r'^$', views.index, name = 'index'),
        url(r'^major/(?P<major_name_url>\w+)/$', views.major, name = 'major'),
        url(r'^about$', views.about, name = 'about'),
        url(r'^contact$', views.contact, name = 'contact'),
        )