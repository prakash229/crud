from django.contrib import admin
from django.urls import path, include
from api1 import views
urlpatterns = [
    path('', views.index),
    path('taskdelete', views.taskdelete),
    path('taskdone', views.taskdone),
    path('addtask', views.addnewtask, name='addtask'),
    path('searchtask', views.searchtask),
    path('searchpage', views.searchpage),
]
