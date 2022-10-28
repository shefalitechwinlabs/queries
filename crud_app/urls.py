from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [

    path('', views.home, name='home'),
    #path('authorform/', views.authorform,name='authorform'),
    path('article/', views.article, name='article'),
    #path('entryform/', views.entryform,name='entryform'),
    path('blogform/', views.blogform,name='blogform'),
    path('table/', views.table,name='table'),
    path('updatetable/<id>', views.update_table,name='updatetable'),
    path('delete/<id>', views.delete,name='delete'),  
]
