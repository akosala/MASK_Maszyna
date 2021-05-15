from django.urls import path, include
from django.conf.urls import url
from django.contrib import admin
from .import views

app_name='mask'

urlpatterns =[
    path('', views.index, name='index'),
    path('kontrah/', views.kontrah_add,name='kontrah_add'),
    url('^loguj/$', views.loguj, name='loguj'),
    url(r'^wyloguj/$', views.wyloguj, name='wyloguj'),
    #path('<int:pytanie_id>/us', views.US, name='us'),
   # path('<int:pytanie_id>/kontrahenci', views.Kontrah, name='kontrahenci')
]