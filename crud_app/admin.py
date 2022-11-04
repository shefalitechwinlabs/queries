from django.contrib import admin
from crud_app.models import *
from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.models import FlatPage


# Define a new FlatPageAdmin
class FlatPageAdmin(FlatPageAdmin):
    fieldsets = (
        (None, {'fields': ('url', 'title', 'content', 'sites')}),
    )

# Re-register FlatPageAdmin
admin.site.unregister(FlatPage)
admin.site.register(FlatPage, FlatPageAdmin)

# Define custom tags for Blog model
class BlogAdmin(admin.ModelAdmin):
  list_display = ['blog_name', 'created_by']
  fields = ('created_by', 'headline', 'blog_name', 'body_text')
  search_fields = ['created_by', 'headline']
  list_filter = ['created_by']

# Define custom tags for Entry model
class EntryAdmin(admin.ModelAdmin):
  list_display = ['created_by', 'pub_date']
  fields = ('pub_date', 'created_by', 'blog',)
  readonly_fields = [('pub_date')]
  DATE_FORMAT = (( 'd/m/Y' ))
  search_fields = ['blog']
  list_filter = ['pub_date', 'created_by']

# Register models
admin.site.register(Blog, BlogAdmin)
admin.site.register(Entry, EntryAdmin)
