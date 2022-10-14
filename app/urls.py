from django.contrib import admin
from django.urls import path
from . import views
app_name='app'
urlpatterns = [
    
    path('home/',views.index,name="index"),
    path('hainame/<name>',views.hainame,name="index"),
    path('add/<a>/<b>',views.add,name='add'),
    path('temp/',views.tempdemo,name='demo'),
     path('tempo/',views.tempo,name='demos'),
     path('homepage',views.ind,name='myhome'),
     path('base',views.base,name='base'),
     path('myhome',views.myhome,name='abhome'),
     path('register',views.register,name='register')
]
