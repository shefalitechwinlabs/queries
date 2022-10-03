from django.contrib import admin
from .models import Practice
 
@admin.register(Practice)
class RequestDemoAdmin(admin.ModelAdmin):
  list_display = ['fullname', 'phonenumber','address', 'zipcode']