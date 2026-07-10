from django.contrib import admin
from django.urls import path,include,re_path
from . import views

urlpatterns = [

    path('test/',views.test),

    re_path('^$',views.home)


]