from django.contrib import admin
from crud_app.models import *

@admin.register(Blog)
class RequestDemoAdmin(admin.ModelAdmin):
  list_Author = ['blog_name','tagline']

@admin.register(Author)
class RequestDemoAdmin(admin.ModelAdmin):
  list_Publisher = ['author_name','email']

@admin.register(Entry)
class RequestDemoAdmin(admin.ModelAdmin):
  list_Books = ['blog', 'headline', 'body_text', 'pub_date','mod_date', 'authors', 'number_of_comments', 'number_of_pingbacks', 'ratings']

@admin.register(ThemeBlog)
class RequestDemoAdmin(admin.ModelAdmin):
  list_Author = ['theme']

admin.site.register(Test)
