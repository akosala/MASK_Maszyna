from django.urls import path, include
from django.conf.urls import url
from django.contrib import admin
from .import views


app_name='mask'

urlpatterns =[
    path('', views.index, name='index'),
    path('kontrah/', views.kontrah_add,name='kontrah_add'),
    path('zus/', views.zusaddoperations, name="zusaddoperations"),
    path('us/', views.usaddoperations, name="usaddoperations"),
    url('^omask/$', views.omask, name="omask"),
    url('^widokzus/<int:pk>/$', views.widokzus, name='widokzus'),
    url('^loguj/$', views.loguj, name='loguj'),
    url(r'^wyloguj/$', views.wyloguj, name='wyloguj'),



]