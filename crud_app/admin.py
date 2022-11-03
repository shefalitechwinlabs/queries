from django.contrib import admin
from crud_app.models import *
import datetime

class BlogAdmin(admin.ModelAdmin):
  list_display = ['blog_name', 'created_by']
  fields = ('created_by', 'headline', 'blog_name', 'body_text')
  search_fields = ['created_by', 'headline']
  list_filter = ['created_by']

class EntryAdmin(admin.ModelAdmin):
  list_display = ['created_by', 'pub_date']
  fields = ('pub_date', 'created_by', 'blog',)
  readonly_fields = [('pub_date')]
  DATE_FORMAT = (( 'd/m/Y' ))
  search_fields = ['blog']
  list_filter = ['pub_date', 'created_by']
  

admin.site.register(Blog, BlogAdmin)
admin.site.register(Entry, EntryAdmin)
