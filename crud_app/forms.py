from django import forms
from .models import *


class BlogForm(forms.ModelForm):

    # Excluded one field
    class Meta:
        model = Blog
        exclude = ['created_by']
