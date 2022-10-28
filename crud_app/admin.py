from django.contrib import admin
from crud_app.models import *

@admin.register(Blog)
class RequestDemoAdmin(admin.ModelAdmin):
  list_Author = ['blog_name','tagline', 'headline', 'body_text']

@admin.register(Entry)
class RequestDemoAdmin(admin.ModelAdmin):
  list_Books = ['blog', 'headline', 'body_text', 'pub_date','mod_date']
