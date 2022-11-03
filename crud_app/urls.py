from django.contrib import admin
from django.urls import path
from . import views

# admin.site.site_header = 'Welcome to Blog Portal'
# admin.site.site_title = 'Login Portal'
# admin.site.index_title = 'Blog Portal'

urlpatterns = [

    path('', views.home, name='home'),
    path('<blog_name>', views.article, name='article'),
    path('blogform/', views.blogform,name='blogform'),
    path('table/', views.table,name='table'),
    path('updatetable/<id>', views.update_table,name='updatetable'),
    path('delete/<id>', views.delete,name='delete'),  
]

