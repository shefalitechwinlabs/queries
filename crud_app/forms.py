from django import forms
from .models import *

class BlogForm(forms.ModelForm):

    class Meta:
        model = Blog
        exclude = ['created_by']
