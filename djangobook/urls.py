"""djangobook URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include,re_path

import app01
from app01 import urls
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('app01/',include(app01.urls)),

    re_path('^$',views.home),

    path('book/list',views.book_list,name='book_list'),
    path('book/add',views.book_add,name='book_add'),
    re_path('book/edit/(?P<edit_id>\d+)', views.book_edit, name='book_edit'),
    re_path('book/delete/(?P<delete_id>\d+)', views.book_delete, name='book_delete'),

    path('publish/list/', views.publish_list, name='publish_list'),
    path('publish/add/',views.publish_add,name='publish_add'),
    re_path('publish/edit/(?P<publish_id>\d+)', views.publish_edit, name='publish_edit'),
    re_path('publish/delete/(?P<delete_id>\d+)', views.publish_delete, name='publish_delete'),

    path('author/list/', views.author_list, name='author_list'),
path('author/add/',views.author_add,name='author_add'),
re_path('author/edit/(?P<author_id>\d+)', views.author_edit, name='author_edit'),
 # 删除作者
re_path('author/delete/(?P<delete_id>\d+)', views.author_delete, name='author_delete'),




]
