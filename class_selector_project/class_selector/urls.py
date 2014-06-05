from django.conf.urls import patterns, url
from class_selector import views

urlpatterns = patterns('', 
        url(r'^$', views.index, name = 'index'),
        url(r'^anthropology/', views.anthropology, name = 'anthropology'),
        url(r'^americanstudies/', views.americanstudies, name = 'americanstudies'),
        )